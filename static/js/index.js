$(function() {
    /* 初期表示時 */
    ajax();

    /* 表示ボタン押下時 */
    $('#view').click(function(){
        console.log('ajax start');
        ajax();
    });
});
/* Ajaxでチャートデータを取得 */
function ajax() {
    var data_type = $('#data-type').val();
    var source_name = $('#source-name').val();
    var start_date = $('#start-date').val();
    var end_date = $('#end-date').val();
    console.log(data_type);
    console.log(source_name);
    console.log(start_date);
    console.log(end_date);
    $.ajax({
        url:'chart',
        type:'GET',
        data:{
            'data_type': data_type,
            'source_name': source_name,
            'start_date': start_date,
            'end_date': end_date
        }
    })
    .done(function(res){
        if(res.result == 'OK') {
            drawChart(res.data);
        }
        else {
            $('#msg').html(res.result);
        }
    })
    .error(function(){
            $('#msg').html('システムエラーが発生しました。');
    })
}

/* チャート描画 */
function drawChart(data) {
    var ctx = $('#canvas').get(0).getContext('2d');
    var labels = data[0].source_names[0].dates;
    var values = data[0].source_names[0].values;
    console.log('labels:');
    console.log(labels);
    console.log('values:');
    console.log(values);
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: data[0].data_type + ' ' + data[0].source_names[0].source_name,
                data: values,
                backgroundColor: "rgba(153,255,0,0.4)"
            }]
        }
    });
}