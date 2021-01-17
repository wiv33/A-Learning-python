import pandas as pd
from tensorflow.keras import models, layers, datasets

(독립, 종속), _ = datasets.cifar10.load_data()
종속 = pd.get_dummies(종속.reshape(-1, ))
print(종속.shape)

X = layers.Input(독립.shape[1:])
H = layers.Conv2D(filters=3, kernel_size=(5, 5), activation='swish')(X)
H = layers.MaxPooling2D()(H)
H = layers.Conv2D(filters=6, kernel_size=(5, 5), activation='swish')(H)
H = layers.MaxPooling2D()(H)

H = layers.Flatten()(H)
H = layers.Dense(120, activation='swish')(H)
H = layers.Dense(84, activation='swish')(H)
Y = layers.Dense(10, activation='softmax')(H)

model = models.Model(X, Y)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(독립, 종속,
                    epochs=10,
                    batch_size=64)


