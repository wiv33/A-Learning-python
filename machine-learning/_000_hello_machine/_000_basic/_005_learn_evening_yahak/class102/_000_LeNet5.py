import pandas as pd
from tensorflow.keras import models, layers, datasets, optimizers

(독립, 종속), (x_test, y_test) = datasets.mnist.load_data()
독립 = 독립.reshape(60000, 28, 28, 1)
종속 = pd.get_dummies(종속)
print(종속.shape)

X = layers.Input(독립.shape[1:])
H = layers.Conv2D(filters=3, kernel_size=(5, 5), padding='same', activation='swish')(X)
H = layers.MaxPooling2D()(H)
H = layers.Conv2D(filters=6, kernel_size=(5, 5), activation='swish')(H)
H = layers.MaxPooling2D()(H)

H = layers.Flatten()(H)
H = layers.Dropout(0.3)(H)
H = layers.Dense(120, activation='swish')(H)
H = layers.Dense(84, activation='swish')(H)
Y = layers.Dense(10, activation='softmax')(H)

model = models.Model(X, Y)
model.compile(optimizer=optimizers.Adam(),
              # optimizer=optimizers.Adagrad(),
              loss='categorical_crossentropy',
              metrics=['accuracy', 'mse'])

history = model.fit(독립, 종속,
                    epochs=10,
                    batch_size=64)


