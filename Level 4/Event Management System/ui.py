import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import traceback
import subprocess
import platform
import sqlite3
import sys

# Refined Color Palette
PRIMARY_COLOR = "#2C3E50"
SECONDARY_COLOR = "#34495E"
ACCENT_COLOR = "#ECF0F1"
BUTTON_COLOR = "#2980B9"
TEXT_COLOR = "#2C3E50"

# Function to display error messages
def show_error(error):
    messagebox.showerror("Error", str(error))
    traceback.print_exc()

# Function to handle ticket purchase by launching ui2.py with event data
def purchase_ticket(event):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ticket_booking_path = os.path.abspath(os.path.join(current_dir, "ui2.py"))
    
    print("Launching:", ticket_booking_path)
    
    try:
        required_fields = ["title", "date", "time", "location", "ticket_price", "available_tickets"]
        if not all(field in event for field in required_fields):
            raise ValueError("Missing required event information")
        
        ticket_price = str(event["ticket_price"])
        available_tickets = str(event["available_tickets"])
        
        print("Event data:", event)
        
        subprocess.Popen([
            sys.executable, ticket_booking_path,
            event["title"],
            event["date"],
            event["time"],
            event["location"],
            ticket_price,
            available_tickets,
        ])
    except Exception as e:
        show_error(f"Error launching ticket purchase: {str(e)}")

# Function to handle menu item clicks
def handle_menu_click(item):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if item == "Tickets":
        tickets_path = os.path.abspath(os.path.join(current_dir, "ticket.py"))
        try:
            subprocess.Popen([sys.executable, tickets_path])
        except Exception as e:
            show_error(f"Error launching ticket.py: {str(e)}")
    elif item == "My Account":
        main_path = os.path.abspath(os.path.join(current_dir, "main.py"))
        try:
            subprocess.Popen([sys.executable, main_path])
        except Exception as e:
            show_error(f"Error launching main.py: {str(e)}")
    else:
        messagebox.showinfo("Info", f"{item} menu item clicked!")

# Function to calculate the number of columns based on the window width
def get_number_of_columns():
    screen_width = root.winfo_width()
    if screen_width >= 1200:
        return 3
    elif screen_width >= 800:
        return 2
    return 1

# Function to update event cards
def update_event_cards():
    for widget in container.winfo_children():
        widget.destroy()

    num_columns = get_number_of_columns()
    for i, event in enumerate(events):
        row, column = divmod(i, num_columns)
        card = create_event_card(container, event)
        card.grid(row=row, column=column, padx=15, pady=20, sticky="nsew")
        container.grid_columnconfigure(column, weight=1)
        container.grid_rowconfigure(row, weight=1)

# Function to create an event card
def create_event_card(parent, event):
    card = tk.Frame(parent, bg="white", relief=tk.FLAT, borderwidth=1,
                    highlightthickness=1, highlightbackground=SECONDARY_COLOR, padx=20, pady=20)
    card.config(width=530, height=700)
    card.grid_propagate(False)

    content_frame = tk.Frame(card, bg="white")
    content_frame.pack(fill=tk.BOTH, expand=True)

    # Image handling
    try:
        img_path = event.get("image", "")
        if img_path and os.path.exists(img_path):
            img = Image.open(img_path).resize((530, 300), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            image_label = tk.Label(content_frame, image=img, bg="white")
            image_label.image = img
            image_label.pack(pady=10)
        else:
            placeholder_label = tk.Label(content_frame, text="No Image Available", 
                                       bg="white", fg=TEXT_COLOR, height=10)
            placeholder_label.pack(pady=10)
    except Exception as e:
        tk.Label(content_frame, text=f"Image Error: {str(e)}", 
                bg="white", fg="red").pack(pady=5)

    # Info section
    info_frame = tk.Frame(content_frame, bg="white")
    info_frame.pack(fill=tk.X, padx=15, pady=10)

    tk.Label(info_frame, text=event["date"], bg="white", 
            fg=BUTTON_COLOR, font=("Helvetica", 16)).pack(fill=tk.X)
    tk.Label(info_frame, text=event["title"], bg="white", 
            fg=PRIMARY_COLOR, font=("Helvetica", 18)).pack(fill=tk.X, pady=(5, 0))
    tk.Label(info_frame, text=event["time"], bg="white", 
            fg=TEXT_COLOR, font=("Helvetica", 12)).pack(fill=tk.X)
    tk.Label(info_frame, text=event["location"], bg="white", 
            fg=TEXT_COLOR, font=("Helvetica", 12)).pack(fill=tk.X)

    # Bottom section
    bottom_frame = tk.Frame(content_frame, bg="white")
    bottom_frame.pack(fill=tk.X, padx=15, pady=(10, 0))

    # Format price with proper currency
    price_text = f"NPR {float(event['ticket_price']):,.2f}"
    tk.Label(bottom_frame, text=price_text, bg="white", 
            fg=BUTTON_COLOR, font=("Helvetica", 14)).pack(side=tk.LEFT)

    # Add tickets available info
    tickets_text = f"Available: {event['available_tickets']}"
    tk.Label(bottom_frame, text=tickets_text, bg="white", 
            fg=TEXT_COLOR, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=10)

    # Buy button
    buy_button = tk.Button(
        bottom_frame,
        text="Buy Tickets",
        bg=BUTTON_COLOR,
        fg=ACCENT_COLOR,
        font=("Helvetica", 12),
        command=lambda e=event: purchase_ticket(e)
    )
    buy_button.pack(side=tk.RIGHT)

    return card

# Function to fetch events from database
def fetch_events_from_db():
    db_events = []
    try:
        conn = sqlite3.connect('samaaye_events.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT title, date, time, location, ticket_price, 
                   available_tickets, image_path 
            FROM events
        ''')
        
        rows = cursor.fetchall()
        conn.close()
        
        for row in rows:
            event = {
                "title": row[0],
                "date": row[1],
                "time": row[2],
                "location": row[3],
                "ticket_price": float(row[4]) if row[4] else 0.0,
                "available_tickets": int(row[5]) if row[5] else 0,
                "image": row[6] if row[6] and os.path.exists(row[6]) else ""
            }
            db_events.append(event)
            
    except sqlite3.Error as e:
        show_error(f"Database Error: {str(e)}")
        traceback.print_exc()
    return db_events

# Main Application
try:
    root = tk.Tk()
    root.title("Samaaye Interactives")

    # Set window state based on the operating system
    if platform.system() == "Windows":
        root.state('zoomed')
    elif platform.system() == "Darwin":  # macOS
        root.attributes('-fullscreen', True)
    elif platform.system() == "Linux":
        root.attributes('-zoomed', True)
    else:
        root.geometry("1200x800")

    root.configure(bg=ACCENT_COLOR)

    # Create header
    header = tk.Frame(root, bg=PRIMARY_COLOR, height=80)
    header.grid(row=0, column=0, sticky="ew")

    # Add logo image instead of text
    try:
        logo_path = "Samaaye Interactives.jpg"
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((150, 80), Image.LANCZOS)
            logo_img = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(header, image=logo_img, bg=PRIMARY_COLOR)
            logo_label.image = logo_img
            logo_label.pack(side=tk.LEFT, padx=30, pady=20)
        else:
            tk.Label(header, text="Logo Not Found", bg=PRIMARY_COLOR, fg="red", font=("Helvetica", 16)).pack(side=tk.LEFT, padx=30)
    except Exception as e:
        show_error(f"Error loading logo: {e}")

    menu = tk.Frame(header, bg=PRIMARY_COLOR)
    menu.pack(side=tk.RIGHT, padx=30)

    for menu_item in ["Events", "Tickets", "My Account"]:
        menu_label = tk.Label(menu, text=menu_item, bg=PRIMARY_COLOR, fg=ACCENT_COLOR, font=("Helvetica", 14))
        menu_label.pack(side=tk.LEFT, padx=20)
        menu_label.bind("<Button-1>", lambda e, item=menu_item: handle_menu_click(item))

    title = tk.Label(root, text="Upcoming Events", bg=ACCENT_COLOR, fg=PRIMARY_COLOR, font=("Helvetica", 32))
    title.grid(row=1, column=0, pady=30)

    # Create scrollable canvas
    canvas = tk.Canvas(root, bg=ACCENT_COLOR, width=1550)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    container = tk.Frame(scrollable_frame, bg=ACCENT_COLOR)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=2, column=0, sticky="nsew")
    scrollbar.grid(row=2, column=1, sticky="ns")

    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=0)

    # Initialize events
    events = []

    # Add hardcoded events
    hardcoded_events = [
        {"title": "The Big 3 (2nd Show)", "date": "5 Dec", "time": "6:00 PM onwards", "location": "LOD, Thamel",
         "image": "abc.png", "ticket_price": 500, "available_tickets": 100},
        {"title": "Nepal Premier League", "date": "19 Dec", "time": "9:15 AM onwards", "location": "TU Cricket Ground",
         "image": "npl.png", "ticket_price": 750, "available_tickets": 250},
        {"title": "Grasslands Carnival", "date": "5 Dec", "time": "4:30 PM onwards", "location": "Patan Durbar Square",
         "image": "grass.jpg", "ticket_price": 350, "available_tickets": 75},
        {"title": "Tech Conference 2025", "date": "23 Dec", "time": "9:00 AM onwards", "location": "Kathmandu",
         "image": "maxresdefault.png", "ticket_price": 800, "available_tickets": 200},
        {"title": "New Year's Eve Party", "date": "31 Dec", "time": "10:00 PM onwards", "location": "City Hall",
         "image": "TentCardversion.png", "ticket_price": 1200, "available_tickets": 500},
    ]

    events.extend(hardcoded_events)
    seen_titles = set(event["title"] for event in events)
    
    db_events = fetch_events_from_db()
    for event in db_events:
        if event["title"] not in seen_titles:
            events.append(event)
            seen_titles.add(event["title"])

    update_event_cards()  # Initial render of events
    root.bind("<Configure>", lambda e: update_event_cards() if e.widget == root else None)

    root.mainloop()

except Exception as e:
    show_error(e)