-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

SELECT name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE day = "28" AND month = 7 AND year = 2021 AND hour = 10 AND minute >= 15 AND minute < 25 AND activity = 'exit';

SELECT activity FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute = 20;

SELECT name FROM people JOIN bank_accounts on people.id = bank_accounts.person_id JOIN atm_transactions on bank_accounts.account_number = atm_transactions.account_number WHERE day = 28 AND year = 2021 AND month = 7 AND atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw';

SELECT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

SELECT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

SELECT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE name = "Bruce");

SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE flights.id = 36);

SELECT hour, minute FROM flights WHERE year = 2021 AND day = 29 AND month = 7 ORDER BY hour, minute LIMIT 1;

SELECT id FROM flights WHERE hour = 8 AND minute = 20;

SELECT name FROM people JOIN passengers on people.passport_number = passengers.passport_number JOIN flights on passengers.flight_id = flights.id WHERE passengers.flight_id = 36;
