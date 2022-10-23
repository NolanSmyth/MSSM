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
    # "patience": 30,
    "patience": 200,
    # "eval_interval": 100,
    "eval_interval": 50,
    # Dataloader hyperparameters
    # "batch_size": 256,
    "batch_size": 64,
    "train_split": 0.95,
    "num_workers": 0,
    "add_noise": True,
    # Sequential hyperparameters
    "num_rounds": 10,
    "num_initial_samples": 500,
    # "num_samples_per_round": 1000 // 10,
    "num_samples_per_round": 5000,
    "num_warmup_per_round": 2000,
    # "num_warmup_per_round": 200,
    "num_chains": 16,
    "logger": None,
}
