#!/usr/bin/env python
"""Client startup routines."""

from grr_response_client import client_logging
from grr.core.grr_response_core import config
from grr.core.grr_response_core.config import contexts
from grr.core.grr_response_core.lib import config_lib
from grr.core.grr_response_core.lib import registry
from grr.core.grr_response_core.lib import stats


def ClientInit():
  """Run all startup routines for the client."""
  if stats.STATS is None:
    stats.STATS = stats.StatsCollector()

  config_lib.SetPlatformArchContext()
  config_lib.ParseConfigCommandLine()

  client_logging.LogInit()
  registry.Init()

  if not config.CONFIG.ContextApplied(contexts.CLIENT_BUILD_CONTEXT):
    config.CONFIG.Persist("Client.labels")
    config.CONFIG.Persist("Client.proxy_servers")
    config.CONFIG.Persist("Client.tempdir_roots")
