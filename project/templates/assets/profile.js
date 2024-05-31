const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

$('.open-update-modal').click(function() {
    var flashcard_id = $(this).data('flashcard-id');
    var question = $(this).data('question');
    var answer = $(this).data('answer');
    var topic = $(this).data('topic');
    
    $('#flashcard_id').val(flashcard_id);
    $('#updateModal #question').val(question);
    $('#updateModal #answer').val(answer);
    $('#updateModal #topic').val(topic);
    
    $('#updateModal').modal('show');
});