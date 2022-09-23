# install python versi 3 terbaru

# Arahkan terminal ke folder project script

# buat environment (jalanakan di terminal)
python3 -m venv Env

# jalankan environment windows (jalankan di terminal)
source Env\\scripts\\activate

# jalankan environment linux (jalanakan di terminal)
source Env/bin/activate

# install dependency (jalankan di terminal)
pip --no-cache-dir install -r requirements.txt

# jalankan script (jalanakan di terminal)
python main.py

struktur folder:

	folder script:
	    	       - main.py <- script
	    	       - /data <- output
	    	       - pdf.pdf <- input / rek koran
	    	       - data.xlsx <- daftar kode unit
	    	       - /Env <- folder environment
	    	       - requirements.txt <- dependency
	    	       - README.txt
