set ns [new Simulator]
$ns color 1 Blue

set nf [open out2.nam w]
$ns namtrace-all $nf

set nf1 [open a2.tr w]
$ns trace-all $nf1

proc finish {} {
	global ns nf
	$ns flush-trace
	close $nf
	exec nam out2.nam &
	exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

$ns duplex-link $n0 $n1 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 1.7Mb 10ms DropTail

$ns duplex-link-op $n0 $n1 orient right-up
$ns duplex-link-op $n1 $n2 orient right-down

$ns duplex-link-op $n1 $n2 queuePos 0.5


$ns queue-limit $n1 $n2 5
set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n2 $sink
$ns connect $tcp $sink
$tcp set fid_ 1


set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

$ns at 0.2 "$ftp start"
$ns at 2.5 "$ftp stop"
$ns at 3.0 "finish"

$ns run






