# QA3Tier Project Setup

## Prerequisites

- Python 3.x installed on your system.
- Git installed on your system.

## Setup Instructions

1. Open a terminal or command prompt.

2. Navigate to your desired location where you want to clone the repository:

    ```bash
    cd ToYourDesiredLocation
    ```

3. Clone the QA3Tier repository:

    ```bash
    git clone https://github.com/iammrunu/qa3tier.git
    ```

4. Create a virtual environment named `qa3tier`:

    ```bash
    python -m venv qa3tier
    ```

5. Activate the virtual environment:

    - On Windows:

        ```bash
        .\qa3tier\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source qa3tier/bin/activate
        ```

6. Change into the `qa3tier` directory:

    ```bash
    cd qa3tier
    ```

7. Install project dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

8. Start the application using `waitress-serve`:

    ```bash
    waitress-serve --host 127.0.0.1 --port 5000 webapp:app
    ```

   The application should now be running locally at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Additional Information

- Ensure that the virtual environment is activated whenever you work on the project.

    ```bash
    # On Windows
    .\qa3tier\Scripts\activate

    # On Unix or MacOS
    source qa3tier/bin/activate
    ```

- If you encounter any issues or errors during setup, refer to the project documentation or contact the project maintainers for assistance.
