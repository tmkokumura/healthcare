/* 初期表示時 */
$(function() {
    ajax();
});

/* 表示ボタン押下時 */
$('#view').click(function(){
    ajax();
});

/* Ajaxでチャートデータを取得 */
function ajax() {
    $.ajax({
        url:'chart',
        type:'GET',
        data:{
            'start-date': $('#start-date').val(),
            'end-date': $('#end-date').val()
            'data-type': $('#data-type').val(),
        }
    })
    .done((data) => {
        drawChart(data);
    })
}

/* チャート描画 */
function drawChart(data) {
    var ctx = $('#canvas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: label.split(','),
            datasets: [{
                label: 'temp',
                data: temp.split(','),
                backgroundColor: "rgba(153,255,0,0.4)"
            },{
                label: 'pressure',
                data: pressure.split(','),
                backgroundColor: "rgba(255,0,153,0.4)"
            },{
                label: 'humidity',
                data: humidity.split(','),
                backgroundColor: "rgba(0,153,255,0.4)"
            }]
        }
    });
}