// Define UI elements
let ui = {
    timer: document.getElementById('timer'),
    robotState: document.getElementById('robot-state').firstChild,
    gyro: {
        container: document.getElementById('gyro'),
        val: 0,
        offset: 0,
        visualVal: 0,
        arm: document.getElementById('gyro-arm'),
        number: document.getElementById('gyro-number')
    },
    robotDiagram: {
        arm: document.getElementById('robot-arm')
    },
    forwardCommand: {
        button: document.getElementById('move-forward-button')
    },
    example: {
        button: document.getElementById('example-button'),
        readout: document.getElementById('example-readout').firstChild
    },
    autoSelect: document.getElementById('auto-select'),
    armPosition: document.getElementById('arm-position')
};

// Key Listeners
// NetworkTables.addRobotConnectionListener(onRobotConnection, true);
// Sets function to be called when any NetworkTables key/value changes
NetworkTables.addGlobalListener(onValueChanged, true);

function onValueChanged(key, value, isNew) {
    // Sometimes, NetworkTables will pass booleans as strings. This corrects for that.
    if (value == 'true') {
        value = true;
    } else if (value == 'false') {
        value = false;
    }

    // This switch statement chooses which UI element to update when a NetworkTables variable changes.
    switch (key) {

        case '/SmartDashboard/drive/navx/yaw':
            ui.gyro.val = value;
            ui.gyro.visualVal = Math.floor(ui.gyro.val - ui.gyro.offset);
            if (ui.gyro.visualVal < 0) {
                ui.gyro.visualVal += 360;
            }
            ui.gyro.arm.style.transform = `rotate(${ui.gyro.visualVal}deg)`;
            ui.gyro.number.innerHTML = ui.gyro.visualVal + 'º';
            break;

        case '/SmartDashboard/arm/encoder':
            // 0 is all the way back, 1200 is 45 degrees forward. We don't want it going past that.
            if (value > 1140) {
                value = 1140;
            }
            else if (value < 0) {
                value = 0;
            }
            // Calculate visual rotation of arm
            var armAngle = value * 3 / 20 - 45;
            // Rotate the arm in diagram to match real arm
            ui.robotDiagram.arm.style.transform = `rotate(${armAngle}deg)`;
            break;

        case '/SmartDashboard/forwardCommand':
            if(value) {
                ui.forwardCommand.button.className = 'active';
            } else {
                ui.fowardCommand.button.className = '';
            }
            break;

        case '/SmartDashboard/example_variable':
            ui.example.button.classList.toggle('active', value);
            ui.example.readout.data = 'Value is ' + value;
            break;

        case '/robot/time':
            // This is an example of how a dashboard could display the remaining time in a match.
            // We assume here that value is an integer representing the number of seconds left.
            ui.timer.innerHTML = value < 0 ? '0:00' : Math.floor(value / 60) + ':' + (value % 60 < 10 ? '0' : '') + value % 60;
            break;

        case '/SmartDashboard/autonomous/modes':
            // Clear previous list
            while (ui.autoSelect.firstChild) {
                ui.autoSelect.removeChild(ui.autoSelect.firstChild);
            }
            // Make an option for each autonomous mode and put it in the selector
            for (let i = 0; i < value.length; i++) {
                var option = document.createElement('option');
                option.appendChild(document.createTextNode(value[i]));
                ui.autoSelect.appendChild(option);
            }
            // Set value to the already-selected mode. If there is none, nothing will happen.
            ui.autoSelect.value = NetworkTables.getValue('/SmartDashboard/currentlySelectedMode');
            break;

        case '/SmartDashboard/autonomous/selected':
            ui.autoSelect.value = value;
            break;
    }
}

// Reset gyro value to 0 on click
ui.gyro.container.onclick = function() {
    // Store previous gyro val, will now be subtracted from val for callibration
    ui.gyro.offset = ui.gyro.val;
    // Trigger the gyro to recalculate value.
    updateGyro('/SmartDashboard/drive/navx/yaw', ui.gyro.val);
};
// Update NetworkTables when autonomous selector is changed
ui.autoSelect.onchange = function() {
    NetworkTables.putValue('/SmartDashboard/autonomous/selected', this.value);
};
// Get value of arm height slider when it's adjusted
ui.armPosition.oninput = function() {
    NetworkTables.putValue('/SmartDashboard/arm/encoder', parseInt(this.value));
};
