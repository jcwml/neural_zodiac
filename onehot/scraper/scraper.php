<?php

# github.com/jcwml
# scrapes https://www.astrology-zodiac-signs.com/ [2600:1901:0:2090::]
# generates csv and packed datasets for training a neural network

$z = array("aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces");
$zd = array();

$use_wget = 1;
$output_file = 'zodiacs';

function onehot($str)
{
    GLOBAL $z;
    $r = '';
    $p = explode('-', $str, 2);
    foreach($z as $i)
    {
        if($i == $p[0] || $i == $p[1])
            $r .= '1';
        else
            $r .= '0';
    }
    return $r;
}

function onehot_packed($str)
{
    GLOBAL $z;
    $r = '';
    $p = explode('-', $str, 2);
    foreach($z as $i)
    {
        if($i == $p[0] || $i == $p[1])
            $r .= pack('f', 1.0);
        else
            $r .= pack('f', 0.0);
    }
    return $r;
}

foreach($z as $i)
{
    foreach($z as $j)
    { 
        if(in_array($j, $zd) == true)
            continue;
        
        $pair = $i . '-' . $j;
        $url = 'https://astrology-zodiac-signs.com/compatibility/' . $pair;
        echo $url . "\n";
        $d = '';
        if($use_wget == 0)
        {
            $c = stream_context_create(['http' => ['method' => 'GET', 'header' => ['User-Agent: PHP']]]);
            $d = file_get_contents($url, false, $c);
        }
        else
        {
            @unlink($pair);
            exec('wget ' . $url);
            while(file_exists($pair) == false){sleep(1);}
            $d = file_get_contents($pair);
            unlink($pair);
        }
        $p = stristr($d, '<h2>Summary</h2>');
        $p = stristr($p, '<h3 class="skills-tittle percentual">');
        $p = substr($p, 37);
        $p = explode('<', $p, 2);
        file_put_contents($output_file . '.csv', $pair . ", " . $p[0] . "\n", FILE_APPEND | LOCK_EX);
        file_put_contents($output_file . '_onehot.csv', onehot($pair) . ", " . $p[0] . "\n", FILE_APPEND | LOCK_EX);
        file_put_contents('train_x.dat', onehot_packed($pair), FILE_APPEND | LOCK_EX);
        file_put_contents('train_y.dat', pack('f', rtrim($p[0], "%")), FILE_APPEND | LOCK_EX);
    }
    array_push($zd, $i);
}


?>
