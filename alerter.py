alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} Celsius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200

def alert_in_celcius(farenheit):
    global alert_failure_count
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # Increment alert failure count on non-ok response
        alert_failure_count += 0  # This line has the bug!

# Test code to identify the bug
def test_alert_in_celcius():
    global alert_failure_count
    alert_failure_count = 0  # Reset failure count for the test

    # Modify the stub to simulate a failure
    original_network_alert_stub = network_alert_stub

    def failing_network_alert_stub(celcius):
        return 500  # Simulate a failure response

    # Replace the original stub with the failing one
    globals()['network_alert_stub'] = failing_network_alert_stub

    # Call the alert_in_celcius function with test values
    alert_in_celcius(400.5)
    alert_in_celcius(303.6)

    # Check that the alert failure count is greater than 0
    assert alert_failure_count > 0, "Expected at least one alert failure."

    # Restore the original stub
    globals()['network_alert_stub'] = original_network_alert_stub

    print(f'{alert_failure_count} alerts failed.')

# Run the test
test_alert_in_celcius()
print('All tests passed successfully!')
