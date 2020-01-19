py:
	kaitai-struct-compiler -t python --outdir RigolWFM ksy/wfm1000d.ksy
	kaitai-struct-compiler -t python --outdir RigolWFM ksy/wfm1000e.ksy
	kaitai-struct-compiler -t python --outdir RigolWFM ksy/wfm1000z.ksy
	kaitai-struct-compiler -t python --outdir RigolWFM ksy/wfm4000c.ksy

check:
	ksylint ksy/wfm1000d.ksy
	ksylint ksy/wfm1000e.ksy
	ksylint ksy/wfm1000z.ksy
	ksylint ksy/wfm4000c.ksy

test:
	python3 RigolWFM/wfm_parser.py -t e wfm/DS1102E.wfm
	python3 RigolWFM/wfm_parser.py -t e wfm/DS1052E.wfm
	python3 RigolWFM/wfm_parser.py -t c wfm/DS4022-A.wfm
	python3 RigolWFM/wfm_parser.py -t c wfm/DS4022-B.wfm

clean:
	rm -f RigolWFM/wfm1000d.py 
	rm -f RigolWFM/wfm1000e.py 
	rm -f RigolWFM/wfm1000z.py 
	rm -f RigolWFM/wfm4000c.py
	rm -rf dist
	rm -rf RigolWFM.egg-info
	rm -rf RigolWFM/__pycache__
	
.PHONY: clean test check