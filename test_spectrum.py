from specdal import Collection
from specdal import Spectrum
import os
datadir = "H:/notebooks/PTI/SVC_8203022_IAS/"
f = "spec_0001_moc.sig"
spectrum = Spectrum(filepath=os.path.join(datadir, f))

print(spectrum)

