from abc import abstractmethod
from copy import deepcopy

import rastervision as rv
from rastervision.core.config  import (Config, ConfigBuilder)
from rastervision.protos.label_source_pb2 import LabelSourceConfig as LabelSourceConfigMsg

class LabelSourceConfig(Config):
    def __init__(self,
                 source_type):
        self.source_type = source_type

    def to_proto(self):
        msg = LabelSourceConfigMsg()
        msg.source_type = self.source_type
        return msg

    def builder(self):
        return rv._registry.get_config_builder(rv.LABEL_SOURCE,
                                               self.source_type)(self)

    @abstractmethod
    def create_source(self, task_config, crs_transformer, tmp_dir):
        """Create the Label Source for this configuration.

           Args:
              task_config: The TaskConfig for which this label source is supplying labels.
              crs_transformer: The crs_transformer used by the raster source this
                               label source is describing.
              tmp_dir: The temporary directory to use if files will need to be downloaded,
                       or None if only using local files.
        """
        pass

    @staticmethod
    def builder(source_type):
        return rv._registry.get_config_builder(rv.LABEL_SOURCE, source_type)()

    @staticmethod
    def from_proto(msg):
        """Creates a config from the specificed protobuf message
        """
        return rv._registry.get_config_builder(rv.LABEL_SOURCE, msg.source_type)() \
                           .from_proto(msg) \
                           .build()


class LabelSourceConfigBuilder(ConfigBuilder):
    pass
