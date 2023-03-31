def load_data(signed_folder, unsigned_folder):
    images = []
    labels = []

    for file in os.listdir(signed_folder):
        img_path = os.path.join(signed_folder, file)
        img = cv2.imread(img_path)
        images.append(img)
        labels.append("signed")

    for file in os.listdir(unsigned_folder):
        img_path = os.path.join(unsigned_folder, file)
        img = cv2.imread(img_path)
        images.append(img)
        labels.append("unsigned")

    return images, labels

# Preprocess the data


def preprocess_data(images, labels, img_size=(224, 224)):
    # Resize images and normalize pixel values
    resized_images = [cv2.resize(img, img_size) for img in images]
    X = np.array(resized_images, dtype=np.float32) / 255.0

    # Encode labels
    encoder = LabelEncoder()
    y = encoder.fit_transform(labels)

    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42)

    return X_train, X_val, y_train, y_val

# Create the CNN model


def create_cnn_model(input_shape):
    model = models.Sequential()
    model.add(layers.Conv2D(
        32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(2, activation='softmax'))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(
                      from_logits=True),
                  metrics=['accuracy'])

    return model

# Load images and labels from folders


tf.config.list_physical_devices('GPU')


# Load data
signed_folder = "dataset/signed"
unsigned_folder = "dataset/unsigned/"
images, labels = load_data(signed_folder, unsigned_folder)

# Preprocess data
X_train, X_val, y_train, y_val = preprocess_data(images, labels)

# Create and train the model
input_shape = (224, 224, 3)
model = create_cnn_model(input_shape)
model.fit(X_train, y_train, epochs=120, validation_data=(X_val, y_val))

# Evaluate the model on the training data
train_loss, train_accuracy = model.evaluate(X_train, y_train, verbose=2)

# Display the training accuracy
print(f"Training accuracy: {train_accuracy * 100:.2f}%")

# Evaluate the model on the validation data
train_loss_val, train_accuracy_val = model.evaluate(X_val, y_val, verbose=2)
