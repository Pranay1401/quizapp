let currentDiv = "1"

function checkLast() {
    const lastBtn = document.getElementById('BtnLast');

    if (parseInt(currentDiv) < 2) {
        lastBtn.style.display = "none"
    } else {
        lastBtn.style.display = "block"

    }
}

function lastCard() {

    // console.log("btn pressed")

    const form = document.getElementById('form');
    let nextDiv;
    if (form.checkValidity()) {

        // console.log("btn pressed")

        const form = document.getElementById('form');
        const oldDiv = document.getElementById(currentDiv);

        currentDiv = (parseInt(currentDiv) - 1).toString()
        const submit_btn = document.getElementById(BUTTON);

        nextDiv = document.getElementById(currentDiv)
        if (nextDiv) {
            oldDiv.style.display = "None"
            nextDiv.style.display = "block";
        }
        checkLast()

    } else {
        form.reportValidity()
    }

}


function nextCard() {

    // console.log("btn pressed")

    const form = document.getElementById('form');
    let nextDiv;
    if (form.checkValidity()) {

        const oldDiv = document.getElementById(currentDiv);
        oldDiv.style.display = "None"
        currentDiv = (parseInt(currentDiv) + 1).toString()
        const submit_btn = document.getElementById(BUTTON);

        checkLast()

        nextDiv = document.getElementById(currentDiv)
        if (nextDiv) {
            nextDiv.style.display = "block";
        } else {

            const newDiv = document.createElement("div");
            newDiv.id = currentDiv
            const newQuestion = document.createElement("label");
            newQuestion.innerHTML = "Question " + currentDiv + ":"
            const newQuestionInput = document.createElement("input");
            newQuestionInput.name = "question_" + currentDiv
            newQuestionInput.required = true;
            newQuestionInput.maxLength = 128;
            newQuestionInput.placeholder = "Type your question here (required)"


            const newCorrect = document.createElement("label");
            newCorrect.innerHTML = "Correct answer:"
            const newCorrectInput = document.createElement("input");
            newCorrectInput.required = true;
            newCorrectInput.maxLength = 64;
            newCorrectInput.name = "correct_" + currentDiv
            newCorrectInput.placeholder = "Type your correct answer here (required)"
            const newIncorrect1 = document.createElement("label");
            newIncorrect1.innerHTML = "Incorrect answer:"
            const newIncorrectInput1 = document.createElement("input");
            newIncorrectInput1.required = true;
            newIncorrectInput1.maxLength = 64;
            newIncorrectInput1.name = "option1_" + currentDiv
            newIncorrectInput1.placeholder = "Type your incorrect answer here (required)"
            const newIncorrect2 = document.createElement("label");
            newIncorrect2.innerHTML = "Incorrect answer:"
            const newIncorrectInput2 = document.createElement("input");
            newIncorrectInput2.name = "option2_" + currentDiv;
            newIncorrectInput2.maxLength = 64;
            newIncorrectInput2.placeholder = "Type your incorrect answer here (optional)"
            const newIncorrect3 = document.createElement("label");
            newIncorrect3.innerHTML = "Incorrect answer:"
            const newIncorrectInput3 = document.createElement("input");
            newIncorrectInput3.name = "option3_" + currentDiv
            newIncorrectInput3.maxLength = 64;
            newIncorrectInput3.placeholder = "Type your incorrect answer here (optional)"

            newDiv.appendChild(newQuestion);
            newDiv.appendChild(newQuestionInput);
            newDiv.appendChild(newCorrect);
            newDiv.appendChild(newCorrectInput);
            newDiv.appendChild(newIncorrect1);
            newDiv.appendChild(newIncorrectInput1);
            newDiv.appendChild(newIncorrect2);
            newDiv.appendChild(newIncorrectInput2);
            newDiv.appendChild(newIncorrect3);
            newDiv.appendChild(newIncorrectInput3);

            form.insertBefore(newDiv, oldDiv.nextSibling);
        }

    } else {
        form.reportValidity()
    }

}