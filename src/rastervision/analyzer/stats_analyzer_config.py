import os

import rastervision as rv
from rastervision.analyzer import (AnalyzerConfig, AnalyzerConfigBuilder, StatsAnalyzer)
from rastervision.protos.analyzer_pb2 import AnalyzerConfig as AnalyzerConfigMsg

class StatsAnalyzerConfig(AnalyzerConfig):
    def  __init__(self, stats_uri=None):
        super().__init__(rv.STATS_ANALYZER)
        self.stats_uri = stats_uri

    def create_analyzer(self):
        if not  self.stats_uri:
            raise rv.ConfigError("stat_uri is not set.")
        return StatsAnalyer(self.stats_uri)

    def to_proto(self):
        msg = AnalyzerConfigMsg(analyzer_type=self.transformer_type)
        if self.stats_uri:
            msg.SetField("stats_uri", self.stats_uri)
        return msg

    def builder(self):
        return StatsAnalyzerConfigBuilder(self)

    def preprocess_command(self, command_type, experiment_config, context=[]):
        conf = self
        if command_type == rv.ANALYZE:
            if not self.stats_uri:
                stats_uri = os.path.join(experiment_config.analyze_uri, "stats.json")
                conf = self.builder() \
                           .with_stats_uri(stats_uri) \
                           .build()
        io_def = rv.core.CommandIODefinition(output_uris=[self.stats_uri])
        return (conf, io_def)


class StatsAnalyzerConfigBuilder(AnalyzerConfigBuilder):
    def __init__(self, prev=None):
        config = {}
        if prev:
            config = { "stats_uri": prev.stats_uri }
        super().__init__(StatsTransformerConfig, config)

    @staticmethod
    def from_proto(self, msg):
        b = StatsTransformerConfigBuilder()
        return b.with_stats_uri(msg.stats_uri)

    def with_stats_uri(self, stats_uri):
        """Set the stats_uri.

            Args:
                stats_uri: URI to the stats json to use
        """
        b = deepcopy(self)
        b.config['stats_uri'] = stats_uri
        return b
