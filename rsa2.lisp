(ql:quickload :hackrsa) ;; in my repository, tktools
(ql:quickload :cl-prime) ;; in my repository, tktools

(setf d (hackrsa:wiener-attack n e))
(setf m (mod-expt c d n))
(hackrsa:decode m)
