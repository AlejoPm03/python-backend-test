# python-backend-test

## Description
This is a simple backend test for Python using Django and the Django Rest Framework.

The goal is to create a simple API to manage agriculture producers with the following fields:
 - CPF or CNPJ
 - Producer's Name
 - Farm Name
 - City
 - State
 - Total Farm Area in Hectares
 - Arable Area in Hectares
 - Vegetation Area in Hectares
 - Crops Planted (Soybeans, Corn, Cotton, Coffee, Sugarcane)

With the following rules:
- The user should have the ability to register, edit, and delete rural producers.
- The system must validate incorrectly entered CPF and CNPJ.
- The sum of arable area and vegetation must not exceed the farm's total area.
- Each producer can plant more than one crop on their farm.
- The platform must have a Dashboard that displays:
  - **Total number of farms**
  - **Total farm area in hectares (total area)**
  - **Pie chart by state**
  - **Pie chart by crop**
  - **Pie chart by land use (Arable area and vegetation)**


## Endpoint Description

### Crops
`/crop/`  
Manage the crops that producers can plant. Multiple crops can be associated with the same producer.

### Producers
`/producer/`  
Manage producers. When creating a producer, the system automatically detects whether the identifier is a CPF or CNPJ and validates it. It also checks that the sum of the arable and vegetation areas does not exceed the farm's total area.

### Producer Statistics
- `/producer/by_state/` — Returns the number of producers by state.
- `/producer/by_crop/` — Returns the number of producers by crop.
- `/producer/by_land_use/` — Returns the number of producers by land use (arable area vs. vegetation).
- `/producer/total_producer/` — Returns the total number of producers.
- `/producer/total_area/` — Returns the total area of all producers.

## How to run

Clone the repository

### Configure the environment variables

- `PROJECT_SECRET_KEY` - This is a secret key for your particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

- `PROJECT_ENV` - This field can be one of the following values [dev, staging, productions], when in dev mode, Django will display detailed error pages. If in staging or production, Django will display a simple page for any unhandled exceptions.

- `GOOGLE_CLOUD_PROJECT` - project ID in google cloud

- `GOOGLE_APPLICATION_CREDENTIALS` - The path to your Google Cloud credentials file. This file is used to authenticate your Django server with Google Cloud services when running locally. You can generate this in the service account in google cloud console. Do not commit this file to source control and do not use this env in cloud run containers because its already set in the cloud run environment automatically.

- `GOOGLE_BUCKET_NAME` - The name of your Google Cloud Storage bucket. This is used to store static and media files from the server as well to store custom dynamic storage data.

#### Database settings

- `DB_USE_PROXY` - Boolean value to indicate if the database is running in cloud or locally. If set to true, the database will be running in cloud and the server will use a local proxy to connect to it. If set to false, the database will be running locally and the server will connect to it directly. If set to true you must also set the following two variables [`POSTGRES_INSTANCE_REGION`, `POSTGRES_INSTANCE_NAME`]

- `POSTGRES_INSTANCE_REGION` - The region of your Postgres database in cloud. This is only needed if `DB_USE_PROXY` is set to true.

- `POSTGRES_INSTANCE_NAME` - The name of your Postgres database in cloud. This is only needed if `DB_USE_PROXY` is set to true.

- `POSTGRES_DB` - The name of your Postgres database.

- `POSTGRES_USER` - The username for your Postgres database.

- `POSTGRES_PASSWORD` - The password for your Postgres database.

- `POSTGRES_HOST` - The host of your Postgres database. Usually this is a localhost or an IP address, if running with default docker-compose.yml file should be `postgres_agro_test`

- `POSTGRES_PORT` - The port Postgres is running on. By default, this is 5432.

## Google Cloud credentials

Create a Service Account key with the following roles:

- Storage Object Administrator
- Cloud Run Service Agent
- Secret Manager's Secret Accessor
- Cloud Run Invoker
- Cloud SQL Client
- Service Account User

During the creation of this key, make sure to select JSON as the key type. Once the Service Account key has been generated and downloaded, rename the downloaded JSON file to `google_local_credentials.json` and move it to the `keys` folder in your local copy of this repository.

## Running the Server
With your `.env` file and `keys/` set up, you can start your server. Open a terminal and navigate to your project directory, then run the following command:

```bash
docker-compose up --build
```

This will start up your Django server along with any other services defined in your `docker-compose.yml` file.

## Initial Server Setup
When running the server for the first time, some additional commands need to be run. These commands create a superuser, make migrations and apply them to your database. Run the following commands:

Make migrations:

```bash
docker-compose exec agro_test python manage.py makemigrations
```

Apply migrations:

```bash
docker-compose exec agro_test python manage.py migrate
```

Create a superuser:

```bash
docker-compose exec agro_test python manage.py createsuperuser --username=admin --email=admin@admin.com
```

## Accessing the Server
With your server now running, you can access it by opening your web browser and going to `localhost:8000`.

## Hosted Example

The hosted example is available at:  
- [Swagger Documentation](https://agro-test-455460972979.us-central1.run.app/swagger)  
- [Producers Panel](https://agro-test-455460972979.us-central1.run.app/producer/)  
- [Crops Panel](https://agro-test-455460972979.us-central1.run.app/crop/)  
- [Producers by State Statistics](https://agro-test-455460972979.us-central1.run.app/producer/by_state/)
- [Producers by Crop Statistics](https://agro-test-455460972979.us-central1.run.app/producer/by_crop/)
- [Producers by Land Use Statistics](https://agro-test-455460972979.us-central1.run.app/producer/by_land_use/)
- [Total Producers Statistics](https://agro-test-455460972979.us-central1.run.app/producer/total_producers/)
- [Total Area Statistics](https://agro-test-455460972979.us-central1.run.app/producer/total_area/)

## Running tests
To run the tests, you can run the following command:
It will the following tests:
- Test cpf and cnpj validation
- Test the sum of arable area and vegetation area
- Test the creation of producers
- Test the creation of crops
- Test of relationship between producers and crops
  
```bash
docker-compose exec agro_test python manage.py test apps
```


