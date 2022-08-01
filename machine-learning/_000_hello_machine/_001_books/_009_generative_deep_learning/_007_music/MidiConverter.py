from midi2audio import FluidSynth

muse_root = '/Users/nhn/Documents/MuseScore3/'
FluidSynth('%s사운드폰트/MuseScore_General.sf3' % muse_root)\
    .midi_to_audio('%s/악보들/bwv988.mscx' % muse_root, '%s/result/output.wav' % muse_root)
