from tensorflow import keras
from tensorflow.keras import layers

class BaseModel(object):

    def __init__(self, num_channels: int = 3, w_size: int = 28, h_size: int = 28, num_classes: int = 10):
        self.num_channels = num_channels
        self.w_size = w_size
        self.h_size = h_size
        self.num_classes = num_classes
        
    def _define_model(self):
        
        model = keras.Sequential(
            [   layers.Input((self.w_size, self.h_size, self.num_channels)),
                layers.Conv2D(32, 3, padding="same"),
                layers.Conv2D(64, 3, padding="same"),
                layers.Conv2D(128, 3, padding="same"),
                layers.MaxPooling2D(),
                layers.Conv2D(256, 3, padding="same"),
                layers.MaxPooling2D(),
                layers.Flatten(),
                layers.Dense(512, activation='relu'),
                layers.Dropout(0.5),
                layers.Dense(128, activation='relu'),
                layers.Dropout(0.3),
                layers.Dense(self.num_classes),
            ])

        return model

    def __call__(self, loss, metrics):
        model = self._define_model()

        model.compile(
            optimizer = keras.optimizers.Adam(),
            loss = loss,
            metrics = metrics,
        )

        return model
