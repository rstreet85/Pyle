# Pyle

A Flask app for managing automotive maintenance. Track and plan your vehicle services.

## Usage
### Create Vehicle Profile
Create a profile for each vehicle to track & schedule maintenance. Each profile also holds specifications and features such as:
- Make, Model, Year, and VIN
- Mileage or Hours
- Engine & Powertrain specs
- Fluid types and volumes
- Weight, wheelbase, length

### Enter Vehicle Service Events & Details
For each maintenace event (EX: oil change, spark plug replacement), maintain a local database containing:
- Date & mileage
- Task performed, and by whom
- Part used & expected lifespan
- Any general notes or images related to the job.

### View Full Vehicle Maintenance History and Status
For each vehicle, you can set a custom schedule for tasks based on either mileage or time intervals. The current date & latest mileage will be used to display an approximate status of the part, and upcoming maintenance will be highlighted.

The entire maintenance record can also be view and edited as well.

## Installation
### Docker (Recommended)
1. Clone the repository:
`git clone https://github.com/rstreet85/Pyle.git`

2. Navigate to the project directory and build the Docker image:
`docker build -t pyle-app .`

3. Once built, run a container wih the app (**NOTE** You can map any desired port to the container):
`docker run -d -p 5000:5000 pyle-app`

4. You should now be able to connect to the app at http://localhost:5000 (or other specified port)

**WARNING:** Currently the database is a local SQLite instance stored on the same container as the app.

## License
MIT