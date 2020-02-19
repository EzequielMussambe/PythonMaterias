import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine=create_engine('sqlite:///flights_travilig.db')

db=scoped_session(sessionmaker(bind=engine))

def main():
    flights=db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    #we use fetchall() to get list of vales

    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")

    flight_id=int(input("\nFlight ID: "))
    flight=db.execute("SELECT origin, destination, duraction FROM flights WHERE id=:id",
                    {"id":flight_id}).fetchall()
    
    if flight is None:
        print("Error No such filght")
        return 
if __name__ == "__main__":
     main() 