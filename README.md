[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/mxgxu2b2)

## User Section:

Welcome to the Hiring Module!

This software aims to streamline the hiring process and facilitate the management of shared office resources. With our tool, you can efficiently track the entire hiring cycle until the contract is finalized.

If you're interested in learning more or want to test our demo, please contact us [here](mailto:info@hiringmodule.com).

**Demo Link:** [Hiring Module Demo](https://proyecto-t5.onrender.com)

## Developer Section:

### Overview:

The Hiring Module is developed using Django framework, providing a robust solution for managing hiring processes. The application utilizes PostgreSQL for the primary database, while a temporary SQLite database is used for testing purposes.

### Setup Instructions:

1. Configure environment variables, including database connection details, in the `.env` file.
2. Navigate to the project directory:

    ```bash
    cd hiring_module
    ```

3. Perform database migrations:

    ```bash
    python manage.py makemigrations hiring_app
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Important Notes:

- This codebase serves as a demo and is not intended for production use in critical business operations.
- Developers are encouraged to set up an SMTP server for handling progress notifications and other relevant functionalities.

Thank you for your interest in the Hiring Module! If you have any questions or suggestions for improvement, feel free to reach out to us.
