$(document).ready(function() {
        $('#results').DataTable( {
                dom: 'Bfrtip',
                buttons: [
                        'csv', 'excel'
                ],
                paging: false
        });
});
