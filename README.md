# SmartSeater - Restaurant Management App

SmartSeater is open-source under the [MIT License](./LICENSE).  
Commercial use by organizations exceeding certain thresholds requires a [Commercial License](./COMMERCIAL_LICENSE).  
Contact omnidevsolutionsllc.help@gmail.com for details.

SmartSeater is a comprehensive restaurant management app designed to streamline operations for both employees and managers. It offers a variety of features that enhance scheduling, seating, and real-time reservation management, improving the overall dining experience for customers and staff.

**The user interface and graphics are implemented using Tkinter**, a popular GUI library for Python, which makes it simple to create visually appealing and responsive desktop applications.

## Features

### Employee Features
- **Employee Schedule:** Employees can view and manage their shifts, including swapping, picking up, and dropping shifts.
- **Time Management:** Employees can track their working hours and ensure timely attendance.

### Manager Features
- **Schedule Management:** Managers can create, edit, and manage employee schedules.
- **Labor Tracking:** View real-time labor cost data to make sure staffing levels align with operational needs.

### Seating Management
- **Customized Seating Chart:** Design your restaurant’s floor plan by placing booths and tables of varying sizes (big, small, booths) on a visual layout.
- **Max Capacity Management:** Easily set the max capacity for each booth and table to ensure optimal space management.
- **Real-Time Updates:** As customers reserve seats, the seating chart updates in real time, both online and in-store.

### Customer Features
- **Reservation System:** Customers can reserve seats in advance, ensuring their table is ready when they arrive.

## Technology Stack

- **Programming Language:** Python
- **UI Framework:** Tkinter (for graphical user interface and layout)
- **Backend:** Python-based backend; a desktop application with direct database interaction through custom functions.
- **Database:** SQLite

## Helpful Notes
-As of now, there are 4 test accounts - all credentials are "test" with 2-4 being followed by there respective numbers.
-Test is "Manager", test2 is "Employee", test3 is "Customer", test4 is "Applicant"


## Installation

To get started with **SmartSeater**, follow these steps:

### Clone the repository:
```bash
git clone https://github.com/your-username/smartseater.git

cd smartseater

python -m venv .venv

#Windows
.venv\Scripts\activate

#Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt

python main.py