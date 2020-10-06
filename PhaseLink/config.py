"""
Configuration classes for the PhaseLink phase associator.
"""

import json


class PhaseLinkConfig:
    """
    Required configuration for the PhaseLink Phase Associator tools.
    """
    def __init__(
        self,
        training_dataset_x: str = "train_X.npy",
        training_dataset_y: str = "train_Y.npy",
        max_event_depth: float = 100.0,
        max_pick_error: float = 0.50,
        max_hypo_dist: float = 300.0,
        station_file: str = "station_list.txt",
        n_max_picks: int = 1500,
        t_win: float = 300,
        n_threads: int = 1,
        station_map_file: str = "station_map.pkl",
        sncl_map_file: str = "sncl_map.pkl",
        tt_table: dict = {"P": "tt.pg", "S": "tt.sg"},
        datum: float = 0.0,  # Sealevel
        n_train_samp: int = 10000,
    ):
        self.training_dataset_x = training_dataset_x
        self.training_dataset_y = training_dataset_y
        self.max_event_depth = max_event_depth
        self.max_pick_error = max_pick_error
        self.max_hypo_dist = max_hypo_dist
        self.station_file = station_file
        self.n_max_picks = n_max_picks
        self.t_win = t_win
        self.n_threads = n_threads
        self.station_map_file = station_map_file
        self.sncl_map_file = sncl_map_file
        self.tt_table = tt_table
        self.datum = datum
        self.n_train_samp = n_train_samp

    def write(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.__dict__, f)

    @classmethod
    def read(cls, filename: str):
        with open(filename, "r") as f:
            dict_representation = json.load(f)
        return cls(**dict_representation)
