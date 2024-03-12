document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.workout-days input');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonName = button.value;
            document.querySelector('.workout-days').style.display = 'none';
            document.querySelector(`.${buttonName}-workout`).style.display = 'block';
            document.querySelector(`.muscle-group`).style.display = 'block';
            document.querySelector(`.submit-btn`).style.display = 'block';
        });
    });

    const submitButton = document.querySelector('.submit-btn');
    submitButton.addEventListener('click', function() {
        document.querySelector('.muscle-group').style.display = 'none';
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const muscleGroups = document.querySelectorAll('.muscle-group div');
    muscleGroups.forEach(function(group) {
        group.addEventListener('click', function() {
            const checkbox = group.querySelector('input[type="checkbox"]');
            checkbox.checked = !checkbox.checked;
            
            if (checkbox.checked) {
                group.classList.add('checked-border');
            } else {
                group.classList.remove('checked-border');
            }
        });
    });
});
