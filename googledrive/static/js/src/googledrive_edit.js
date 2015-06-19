function GoogleDriveEditXBlock(runtime, element) {
    $(element).find('.save-button').bind('click', function() {
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');

        var data = {
            title: $(element).find('input[name=title]').val(),
            id: $(element).find('input[name=id]').val(),
        };

        runtime.notify('save', {state: 'start'});
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            runtime.notify('save', {state:'end'});
        });
    });

    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });
}
