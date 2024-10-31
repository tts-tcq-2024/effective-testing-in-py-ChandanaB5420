alert_failure_count = 0

def network_alert_stub(celsius):
    print(f'ALERT: Temperature is {celsius} Celsius')
    # Always return 200 for the stub (for testing purposes, we can modify this)
    return 200

def alert_in_celsius(fahrenheit):
    global alert_failure_count
    celsius = (fahrenheit - 32) * 5 / 9
    return_code = network_alert_stub(celsius)
    if return_code != 200:
        # Increment alert failure count on non-ok response
        alert_failure_count += 0  # This line has the bug!

def test_alert_in_celsius():
    global alert_failure_count
    alert_failure_count = 0  # Reset the failure count for the test

    # Define a failing version of the network alert stub
    def failing_network_alert_stub(celsius):
        return 500  # Simulating a failure response

    # Replace the original stub with the failing one
    original_network_alert_stub = network_alert_stub
    globals()['network_alert_stub'] = failing_network_alert_stub

    # Call the alert function
    alert_in_celsius(400.5)
    alert_in_celsius(303.6)

    # Assert that the alert failure count is greater than 0
    assert alert_failure_count > 0, "Expected at least one alert failure."

    # Restore the original stub
    globals()['network_alert_stub'] = original_network_alert_stub

    print(f'{alert_failure_count} alerts failed.')

# Run the test
test_alert_in_celsius()
print('All tests passed successfully!')
