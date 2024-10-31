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
class AlertSystem:
    def __init__(self):
        self.alert_failure_count = 0

    def real_network_alert(self, celsius):
        print(f"Sending real alert for temperature: {celsius:.1f} Celsius.")
        return 500 if celsius > 200.0 else 200  # 500 for failure, 200 for success

    def network_alert_stub(self, celsius):
        print(f"ALERT: Temperature is {celsius:.1f} Celsius.")
        return 500  # Simulated failure

    def mock_network_alert(self, celsius):
        # Check the Celsius value to ensure correct conversion
        if celsius in {204.7, 150.0}:
            return 200  # Mock success for known correct values
        return 500  # Mock failure for others

    def alert_in_celsius(self, fahrenheit, network_alert):
        celsius = (fahrenheit - 32) * 5 / 9
        return_code = network_alert(celsius)
        if return_code != 200:
            self.alert_failure_count += 1

    def test_alert_in_celsius(self, network_alert):
        self.alert_in_celsius(400.5, network_alert)  # Should trigger a failure
        self.alert_in_celsius(303.6, network_alert)  # Should trigger another failure
        self.alert_in_celsius(212.0, network_alert)  # Should pass (100 Celsius)
        self.alert_in_celsius(32.0, network_alert)    # Should pass (0 Celsius)


if __name__ == "__main__":
    system = AlertSystem()

    # Test with the stub
    system.test_alert_in_celsius(system.network_alert_stub)
    assert system.alert_failure_count == 2  # Expecting 2 failures

    # Reset failure count
    system.alert_failure_count = 0

    # Test with the real alert function
    system.alert_in_celsius(150.0, system.real_network_alert)  # Should succeed
    system.alert_in_celsius(400.5, system.real_network_alert)  # Should fail

    # Check the failure count
    assert system.alert_failure_count == 1  # Expecting 1 failure
    print(f"{system.alert_failure_count} alerts failed.")

    # Test with the mock function to validate conversion
    system.alert_failure_count = 0  # Reset count for conversion test
    system.alert_in_celsius(400.5, system.mock_network_alert)  # Should fail (mock)
    system.alert_in_celsius(303.6, system.mock_network_alert)  # Should fail (mock)
    system.alert_in_celsius(212.0, system.mock_network_alert)   # Should pass (mock)
    system.alert_in_celsius(32.0, system.mock_network_alert)     # Should pass (mock)

    assert system.alert_failure_count == 2  # Expecting 2 failures for mock
    print(f"{system.alert_failure_count} alerts failed during mock test.")
