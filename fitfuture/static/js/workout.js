document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.workout-days button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonName = button.textContent.trim();
            document.querySelector('.workout-days').style.display = 'none';
            document.querySelector(`.${buttonName}-workout`).style.display = 'block';
        });
    });

    const submitButton = document.querySelector('.muscle-group button');
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
