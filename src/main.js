// questions and correctAnswers data arrays are supposed to already be linked to site which uses math tasks logic

let currentTaskIndex = 0;
let totalScore = 0

let taskNumbers = document.querySelector(".example-numbers")

let submitBtn = document.querySelector("#submitAnswer");
let previousQuestionBtn = document.querySelector("#goToPrevious");
let nextQuestionBtn = document.querySelector("#goToNext");
updateTaskIndexDisplayed()

submitBtn.addEventListener("click", function() {
    let userAnswerValue = document.querySelector("#answer").value;
    if (userAnswerValue == "") {
        alert("Don't forget the answer before submiting 😜")
    } else {
        checkUserAnswer(userAnswerValue)
        updateTaskIndexDisplayed()
    }
    if (currentTaskIndex == questions.length - 1) {
        alert(`Congratulations! 🥳
        Total score: ${totalScore}`)
        nextQuestionBtn.disabled = true;
        previousQuestionBtn.disabled = true;
        document.querySelector(".task-description").innerHTML = `You can start once more to get better score and math skill 😎😍`
    }
});
previousQuestionBtn.addEventListener("click", function() {
    document.querySelector("#answer").value = "";
    changeToPreviousTask()
    submitBtn.disabled = false;

});
nextQuestionBtn.addEventListener("click", function() {
    document.querySelector("#answer").value = "";
    changeToNextTask()
    updateTaskIndexDisplayed()
    submitBtn.disabled = false;
});

function checkUserAnswer(ans) {
    console.log(`User said its ${ans}`)
    if (ans == correctAnswerss[currentTaskIndex]) {
        submitBtn.disabled = true;
        document.querySelector(".task-answer-banner").style.backgroundColor = "green";
        document.querySelector(".task-answer-banner").style.display = "flex";
        document.querySelector(".task-answer-banner").innerHTML = `Exactly! 🥳 ${ans} is the correct answer! ✅`
        totalScore += 1
    } else {
        document.querySelector(".task-answer-banner").style.backgroundColor = "red";
        document.querySelector(".task-answer-banner").style.display = "flex";
        document.querySelector(".task-answer-banner").innerHTML = `Not really 😢 ${ans} isn't the one! Try once again 😁❌`
        totalScore -= 1
    }
}

function changeToNextTask() {
    document.querySelector(".task-answer-banner").style.display = "none";
    if (currentTaskIndex == questions.length - 1) {
        console.error("Cannot get more task. That was the last one.")
        return;
    } else {
        currentTaskIndex++;
        taskNumbers.innerHTML = questions[currentTaskIndex]
        console.log(`Correct answer is: ${correctAnswerss[currentTaskIndex]}`)
    }

}

function changeToPreviousTask() {
    document.querySelector(".task-answer-banner").style.display = "none";
    if (currentTaskIndex == 0) {
        console.error("Cannot get task number smaller than 0")
        return;
    } else {
        currentTaskIndex--;
        taskNumbers.innerHTML = questions[currentTaskIndex]
        console.log(`Correct answer is: ${correctAnswerss[currentTaskIndex]}`)
    }
}

function updateTaskIndexDisplayed() {
    document.querySelector(".task-list").innerHTML = `${currentTaskIndex} / ${questions.length -1}`
}