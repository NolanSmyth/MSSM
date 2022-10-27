pipeline_kwargs = {
    # simulator kwargs
    "simulator_kwargs": {"use_direct_detection": False, "use_atlas_constraints": True},
    # Model hyperparameters
    "model_type": "classifier",  # "classifier" or "flow"
    "ensemble_size": 5,
    "num_layers": 3,
    "hidden_dim": 256,
    # flow specific parameters
    "transform_type": "MaskedPiecewiseRationalQuadraticAutoregressiveTransform",
    "permutation": "Conv1x1",
    "tail_bound": 10.0,
    "num_bins": 4,
    # Optimizer hyperparmeters
    "max_norm": 1e-3,
    "learning_rate": 3e-4,
    # "weight_decay": 1e-6,
    "weight_decay": 0,
    # Train hyperparameters
    "nsteps": 250000,
    "patience": 100,
    "eval_interval": 10,
    # "patience": 10,
    # "eval_interval": 10,
    # Dataloader hyperparameters
    "batch_size": 256,
    "train_split": 0.95,
    "num_workers": 0,
    "add_noise": True,
    # Sequential hyperparameters
    "num_rounds": 5,
    # "num_initial_samples": 10,
    "num_initial_samples": 200,
    # "num_samples_per_round": 1000 // 10,
    "num_samples_per_round": 100,
    # "num_warmup_per_round": 10,
    "num_warmup_per_round": 100,
    "num_chains": 20,
    "logger": None,
}
