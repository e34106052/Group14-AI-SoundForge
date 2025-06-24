import random

music_genre_database = {
    # ==================== Blues ====================
    'blues': {
        'Instruments': [
            'electric guitar with heavy vibrato', 'wailing harmonica solo', 'slide guitar (bottleneck)', 
            'upright acoustic bass', 'rolling piano chords', 'resonator guitar', 'drums played with brushes', 
            'Hammond organ swells', 'a single, stomping foot', 'raw male vocals', 'soulful female vocals'
        ],
        'Mood/Atmosphere': [
            'melancholic and soulful', 'gritty and raw', 'a smoky, late-night bar feel', 'heartfelt and storytelling', 
            'world-weary and mournful', 'cathartic and emotional', 'introspective and personal', 
            'stripped-down and honest', 'a sense of struggle and resilience', 'yearning and longing'
        ],
        'Rhythm/Style': [
            'a slow 12/8 shuffle rhythm', 'a classic 12-bar blues structure', 'a walking bassline', 
            'call and response between vocal and guitar', 'a triplet feel (swing eighths)', 'stop-time rhythm', 
            'a simple, repetitive chord progression', 'a raw, unquantized feel', 'boogie-woogie piano rhythm', 'a slow drag'
        ],
        'Tempo': [
            'slow tempo around 60-80 BPM', 'very laid-back walking pace', 'a slow, dragging tempo', 
            'moderately slow', 'adagio blues', 'lento feel', 'gradually building tempo', 'unhurried', 
            'a heavy, plodding pace', 'relaxed and unhurried'
        ],
        'Key': [
            'E blues scale', 'A minor pentatonic scale', 'G major with dominant 7th chords', 
            'use of blue notes (flat 3rd, 5th, 7th)', 'I-IV-V chord progression', 'turnaround progressions', 
            'simple diatonic harmony', 'call and response phrases', 'based on a guitar-friendly key', 'raw, untutored harmony'
        ],
        'Production/Features': [
            'vintage tube amplifier tone with natural overdrive', 'a raw, live-off-the-floor recording feel', 
            'minimal processing and effects', 'audible tape saturation and warmth', 'a mono or narrow stereo field', 
            'recorded in a small, acoustically live room', 'natural reverb', 'gritty, unfiltered sound', 
            'focus on performance over perfection', 'the sound of a small combo band'
        ],
        'Negative Prompts': [
            'NOT pop structure', 'NOT overly polished', 'NO synthesizers', 'NO drum machines', 
            'NO aggressive distortion', 'NOT fast rock tempo', 'NO autotune', 'NO complex orchestral layers',
            'NOT Caribbean style', 'NO major-key pop happiness'
        ]
    },
    # ==================== Classical ====================
    'classical': {
        'Instruments': [
            'a full symphony orchestra', 'a classical string quartet (2 violins, viola, cello)', 'a grand piano concerto',
            'elegant woodwind section (flute, oboe, clarinet)', 'powerful brass fanfare (trumpets, trombones)',
            'thundering timpani drums', 'delicate harp arpeggios', 'a baroque harpsichord', 'a majestic pipe organ',
            'a cappella choir', 'solo cello performance'
        ],
        'Mood/Atmosphere': [
            'elegant and refined', 'dramatic and powerful', 'poignant and beautiful', 'majestic and grand',
            'serene and contemplative', 'epic and adventurous', 'somber and mournful', 'uplifting and triumphant',
            'delicate and intricate', 'passionate and romantic'
        ],
        'Rhythm/Style': [
            'complex baroque counterpoint', 'a flowing and lyrical melodic structure', 'sonata form development',
            'stately and majestic rhythm', 'a graceful waltz time', 'dynamic swells (crescendo and diminuendo)',
            'intricate fugue', 'legato (smooth) and staccato (detached) passages', 'a theme and variations structure', 'rhythmic motifs'
        ],
        'Tempo': [
            'slow Adagio tempo', 'walking pace Andante', 'moderate Moderato', 'fast Allegro', 'very fast Presto',
            'gradual accelerando (speeding up)', 'gradual ritardando (slowing down)', 'Largo (very slow and broad)',
            'Vivace (lively and fast)', 'Grave (very slow, solemn)'
        ],
        'Key': [
            'D major key for triumph', 'C minor key for drama', 'diatonic harmony', 'use of chromaticism for tension',
            'modal interchange', 'perfect cadences for resolution', 'complex chord progressions', 'key modulations',
            'tonal and atonal sections', 'based on traditional Western harmony'
        ],
        'Production/Features': [
            'rich concert hall acoustics and natural reverb', 'a pristine, high-fidelity recording',
            'wide dynamic range (from pianissimo to fortissimo)', 'a wide and deep stereo image',
            'focus on capturing the natural timbre of instruments', 'no artificial effects', 'a clean and uncompressed sound',
            'the sound of a large ensemble in a large space', 'meticulous microphone placement', 'transparent production'
        ],
        'Negative Prompts': [
            'NO electronic beats', 'NO distorted rock guitars', 'NOT repetitive pop structure', 'NO synthesizers',
            'NO heavy compression', 'NOT a 4/4 rock beat', 'NO blues notes', 'NO improvisation',
            'NOT lo-fi', 'NO modern studio effects like flanger or phaser'
        ]
    },
    # ==================== Country ====================
    'country': {
        'Instruments': [
            'acoustic guitar fingerpicking', 'weeping pedal steel guitar', 'lively fiddle melody', 'twangy electric guitar (Telecaster)',
            'driving banjo rolls', 'simple, solid bass guitar', 'storytelling male/female vocals',
            'honky-tonk piano', 'mandolin flourishes', 'harmonica accompaniment', 'brushed snare drum'
        ],
        'Mood/Atmosphere': [
            'nostalgic and storytelling', 'heartfelt and sincere', 'a down-to-earth, rural vibe', 'a sense of longing and heartbreak',
            'patriotic and proud', 'a fun, carefree, party atmosphere', 'introspective and melancholic',
            'simple and honest', 'a road trip feeling', 'a small-town feel'
        ],
        'Rhythm/Style': [
            'a simple, steady 4/4 drum beat ("two-step")', 'a gentle 3/4 waltz time', 'a driving "train beat" rhythm',
            'acoustic rhythm guitar strumming', 'a boom-chick rhythm pattern', 'a slow ballad feel',
            'alternating bass notes', 'a shuffle feel', 'a modern country-rock groove', 'a simple chord progression'
        ],
        'Tempo': [
            'mid-tempo at 90-120 BPM', 'a slow ballad tempo around 70 BPM', 'an upbeat, faster 130 BPM',
            'a relaxed, walking pace', 'a steady, driving tempo', 'a cruising tempo', 'a laid-back feel',
            'a gentle, swaying tempo', 'a toe-tapping tempo', 'a heart-pounding fast tempo'
        ],
        'Key': [
            'G major key', 'C major key', 'D major key', 'simple I-IV-V chord progressions', 'major scale melodies',
            'use of suspended chords', 'vocal harmonies in thirds and fifths', 'a focus on strong, simple melodies',
            'acoustic-guitar-friendly keys', 'straightforward diatonic harmony'
        ],
        'Production/Features': [
            'a warm and organic sound', 'clean and polished modern Nashville production', 'a sense of open space and clarity',
            'natural-sounding vocals front and center', 'twangy guitar tones', 'tight rhythm section',
            'subtle use of reverb and delay', 'a focus on live instrumentation', 'a radio-friendly mix', 'crisp and clear acoustic instruments'
        ],
        'Negative Prompts': [
            'NO heavy distortion', 'NO complex jazz chords', 'NOT electronic dance music', 'NO synthesizers as lead instruments',
            'NO ambient textures', 'NO aggressive screaming vocals', 'NO drum machines', 'NO orchestral strings',
            'NOT minimalist', 'NO atonal or dissonant harmony'
        ]
    },
    # ==================== Disco ====================
    'disco': {
        'Instruments': [
            'a lush orchestral string section', 'powerful brass stabs on the off-beats', 'a syncopated slap bass guitar',
            'funky wah-wah electric guitar chords', 'a four-on-the-floor kick drum', 'an open hi-hat on the off-beat',
            'classic electric piano (Rhodes/Wurlitzer)', 'hand claps and Latin percussion (congas, bongos)',
            'soaring falsetto male vocals', 'powerful female diva vocals', 'synthesizer flourishes'
        ],
        'Mood/Atmosphere': [
            'uplifting, energetic, and danceable', 'glamorous and celebratory', 'joyful and groovy',
            'a vibrant Saturday Night Fever vibe', 'extravagant and luxurious', 'carefree and euphoric',
            'a packed, glittering dance floor feel', 'romantic and sensual', 'funky and soulful', 'feel-good and positive'
        ],
        'Rhythm/Style': [
            'an iconic four-on-the-floor kick drum pattern', 'a syncopated 16th-note hi-hat pattern',
            'a prominent snare or clap on beats 2 and 4', 'an active, melodic bassline', 'a repetitive, hypnotic groove',
            'funky guitar strumming patterns', 'call and response between strings and brass', 'a build-up and release structure',
            'a strong, dance-oriented pulse', 'an irresistibly groovy rhythm'
        ],
        'Tempo': [
            'a steady dance tempo of 120-130 BPM', 'an energetic 125 BPM', 'a solid, driving beat',
            'a consistent, non-changing tempo', 'a classic disco tempo', 'a four-to-the-floor pulse',
            'a fast-paced dance groove', 'a moderate but energetic tempo', 'a pulsating rhythm', 'a hypnotic tempo'
        ],
        'Key': [
            'A minor key', 'C major key', 'modal harmony with 7th and 9th chords', 'simple, memorable chord progressions',
            'catchy, singable melodies', 'use of orchestral stabs for punctuation', 'vocal ad-libs and hooks',
            'a focus on harmonic richness', 'descending basslines', 'a soulful and melodic approach'
        ],
        'Production/Features': [
            'a classic 1970s production style', 'a lush, layered sound with many instruments',
            'heavy use of reverb on vocals and strings', 'a polished, slick studio sound', 'a wide stereo field',
            'a "wall of sound" production', 'phased strings and synth pads', 'a bass-heavy and punchy mix',
            'the sound of a large studio orchestra', 'a bright, treble-heavy mix'
        ],
        'Negative Prompts': [
            'NOT hip-hop', 'NOT rock music', 'NO melancholic or sad mood', 'NO acoustic folk instruments',
            'NO distorted guitars', 'NOT minimalist', 'NO slow ballads', 'NO raw, lo-fi production',
            'NO growling vocals', 'NO complex, changing time signatures'
        ]
    },
    # ==================== Hip Hop ====================
    'hiphop': {
        'Instruments': [
            'a deep 808 kick drum and sub-bass', 'rattling trap-influenced hi-hat rolls', 'a classic boom-bap drum break sample',
            'a sampled soul or jazz melody', 'a simple, repetitive synth lead', 'scratched vinyl sounds from a turntable',
            'an MPC drum machine pattern', 'a sampled vocal chop hook', 'a Roland TR-909 drum machine', 'a simple piano loop'
        ],
        'Mood/Atmosphere': [
            'an urban street atmosphere', 'confident, cool, and boastful', 'an introspective and conscious vibe',
            'a high-energy party feel', 'a dark and gritty mood', 'a chill and relaxed lo-fi feel',
            'a futuristic, trap soundscape', 'a nostalgic, old-school vibe', 'a minimalist and sparse mood', 'a thoughtful and lyrical atmosphere'
        ],
        'Rhythm/Style': [
            'a classic boom-bap drum pattern (kick-snare)', 'modern trap-influenced hi-hat rolls and triplets',
            'a relaxed, unquantized (off-the-grid) beat', 'a strong emphasis on the kick and snare',
            'a syncopated, head-nodding groove', 'a repetitive, looping beat', 'a minimalist rhythmic structure',
            'a heavily swung rhythm', 'a straight, quantized 16th-note rhythm', 'a complex, polyrhythmic beat'
        ],
        'Tempo': [
            'a slow, heavy tempo around 80-95 BPM', 'a faster trap tempo of 130-150 BPM', 'a relaxed lo-fi tempo around 70 BPM',
            'a classic 90s tempo of 95 BPM', 'a half-time feel', 'a double-time feel', 'a very slow, syrupy tempo',
            'a mid-tempo groove', 'a driving, energetic tempo', 'a laid-back, behind-the-beat tempo'
        ],
        'Key': [
            'a minor key for a serious mood', 'a simple, repetitive 2 or 4-bar loop', 'minimal harmonic content',
            'a bassline as the main harmonic driver', 'based on a sampled chord progression', 'a single, repeated chord',
            'a dissonant, atonal melody', 'a pentatonic scale melody', 'a blues-inflected harmony', 'a modal loop'
        ],
        'Production/Features': [
            'a focus on rhythm over melody and harmony', 'a heavily compressed, punchy drum sound',
            'the sound of vinyl crackle and hiss', 'a clean, digital, modern production', 'heavy use of side-chain compression',
            'autotuned and layered vocals', 'a bass-heavy mix', 'a minimalist arrangement', 'a raw, unfiltered sound', 'the use of ad-libs and background vocals'
        ],
        'Negative Prompts': [
            'NO disco strings', 'NO four-on-the-floor rock beats', 'NO country fiddle or steel guitar',
            'NO soaring, complex melodies', 'NO live band feel (usually)', 'NO gentle, acoustic folk sounds',
            'NO classical orchestration', 'NO clean, undistorted electric guitars', 'NOT a swing rhythm', 'NO operatic vocals'
        ]
    },
    # ==================== Jazz ====================
    'jazz': {
        'Instruments': [
            'an improvisational saxophone (tenor/alto) solo', 'a piano "comping" complex chords', 'a walking upright bass line',
            'a drum kit with a focus on ride cymbals', 'a muted trumpet solo (using a Harmon mute)', 'a smooth jazz electric guitar',
            'a big band with a full brass section', 'a vibraphone solo', 'scat singing vocals', 'a Hammond B3 organ', 'a clarinet in a swing style'
        ],
        'Mood/Atmosphere': [
            'sophisticated and cool', 'intimate and relaxed in a smoky club', 'energetic, lively, and swinging',
            'a melancholic, film-noir feel', 'a playful and conversational mood', 'intellectual and complex',
            'a smooth and romantic atmosphere', 'a bluesy and soulful vibe', 'a vibrant and celebratory feel', 'an experimental and free-form mood'
        ],
        'Rhythm/Style': [
            'a classic swing rhythm with a triplet feel', 'a relaxed Bossa Nova groove', 'a fast, complex Bebop rhythm',
            'a funky, fusion rhythm', 'a modal jazz approach with slow harmonic rhythm', 'a free jazz with no set rhythm',
            'call and response between instruments', 'a syncopated and polyrhythmic feel', 'a strong focus on improvisation', 'a "cool jazz" relaxed feel'
        ],
        'Tempo': [
            'a swinging medium tempo of 120-140 BPM', 'a cool, slow ballad tempo around 60 BPM', 'a blazing fast Bebop tempo over 200 BPM',
            'a relaxed Bossa Nova tempo around 80 BPM', 'a mid-tempo "cool jazz" feel', 'a "burning" fast tempo',
            'a slow, sultry tempo', 'a cheerful, upbeat tempo', 'a flexible "rubato" tempo', 'a driving, hard-bop tempo'
        ],
        'Key': [
            'use of extended chords (7ths, 9ths, 13ths)', 'complex chord progressions (ii-V-I)', 'a focus on improvisation over a set of changes',
            'use of the blues scale and blue notes', 'modal harmony (e.g., based on Dorian or Mixolydian modes)',
            'chromaticism and passing chords', 'a sophisticated harmonic language', 'a walking bassline outlining the chords',
            'reharmonization of standards', 'a harmonically dense texture'
        ],
        'Production/Features': [
            'the sound of a live recording in an intimate jazz club', 'a strong improvisational and interactive feel',
            'a warm, analog recording sound', 'a natural and uncompressed sound', 'each instrument clear in the mix',
            'a focus on capturing the performance', 'a classic Blue Note records sound', 'a minimalist "trio" recording',
            'a lush "big band" production', 'a dry mix with minimal reverb'
        ],
        'Negative Prompts': [
            'NO rock guitar distortion', 'NO straight, non-swung 4/4 rock beat', 'NOT quantized or programmed',
            'NO simple I-IV-V pop progressions', 'NO synthesizers', 'NO autotuned vocals', 'NO heavy compression',
            'NO aggressive metal drumming', 'NOT repetitive', 'NO four-on-the-floor kick drum'
        ]
    },
    # ==================== Metal ====================
    'metal': {
        'Instruments': [
            'heavily distorted, palm-muted electric guitars', 'a fast, technical, shredding guitar solo',
            'extremely fast double bass drumming', 'aggressive, guttural, or screaming vocals',
            'a thick, distorted bass guitar tone', 'power chord progressions', 'blast beat drum patterns',
            'a downtuned 7 or 8-string guitar', 'technical, syncopated guitar riffs', 'pinch harmonics and dive bombs', 'a powerful, clean vocal performance (Power Metal)'
        ],
        'Mood/Atmosphere': [
            'aggressive and intense', 'dark, powerful, and epic', 'fast, chaotic, and energetic',
            'rebellious and defiant', 'a feeling of headbanging energy', 'dark and menacing',
            'anthemic and triumphant', 'a technical and precise feel', 'raw and primal', 'a theatrical, gothic atmosphere'
        ],
        'Rhythm/Style': [
            'fast tremolo picking on guitars', 'syncopated, chugging riffs', 'complex and fast drum fills',
            'odd time signatures and changing tempos', 'a driving, relentless rhythm', 'a slow, heavy, doom-laden groove',
            'a galloping rhythm', 'a precise, machine-like rhythm', 'a thrash metal beat', 'a melodic, guitar-harmony-driven style'
        ],
        'Tempo': [
            'a very fast tempo of 160-200+ BPM', 'a heavy, headbanging mid-tempo of 120-140 BPM',
            'a slow, crushing doom metal tempo below 80 BPM', 'a relentless, driving tempo', 'an extremely fast, "blast beat" tempo',
            'a thrash metal tempo around 180 BPM', 'a moderate, groovy tempo', 'abrupt tempo changes',
            'a powerful, marching tempo', 'a chaotic, unpredictable tempo'
        ],
        'Key': [
            'a minor key, often E minor or D minor', 'use of the Phrygian or Locrian modes',
            'dissonant intervals like the tritone', 'chromatic and dissonant riffs', 'a focus on riffs rather than chord progressions',
            'complex, technical song structures', 'guitar harmonies in thirds', 'power chords (root and fifth only)',
            'atonal solos', 'a dark and menacing harmonic palette'
        ],
        'Production/Features': [
            'high-gain guitar distortion (a "wall of sound")', 'a "scooped" midrange EQ on guitars',
            'a loud, heavily compressed mix ("brickwalled")', 'triggered or sample-replaced drums for clarity and power',
            'layered, multi-tracked guitars', 'a bass tone that complements the guitars', 'a modern, polished metal production',
            'a raw, "garage" production feel', 'a clear separation between instruments despite the density', 'a powerful and overwhelming sound'
        ],
        'Negative Prompts': [
            'NO clean, undistorted guitar tones (mostly)', 'NO acoustic folk instruments', 'NOT pop music',
            'NO funky basslines', 'NO gentle, relaxing moods', 'NO simple, major-key melodies', 'NO swing rhythm',
            'NO four-on-the-floor disco beat', 'NO soft, breathy vocals', 'NO unprocessed, natural drums'
        ]
    },
    # ==================== Pop ====================
    'pop': {
        'Instruments': [
            'a catchy lead synthesizer melody', 'clean, arpeggiated electric guitar chords', 'a powerful, layered lead vocal',
            'a steady, four-on-the-floor drum machine beat', 'a punchy, simple bassline that locks with the kick',
            'finger snaps or claps on beats 2 and 4', 'lush synth pads for harmony', 'processed background vocals and ad-libs',
            'an acoustic piano for a ballad', 'a filtered synth intro', 'a sub-bass synth'
        ],
        'Mood/Atmosphere': [
            'bright, commercial, and catchy', 'uplifting and feel-good', 'emotional and heartfelt (for ballads)',
            'a danceable, party vibe', 'a youthful and energetic feel', 'a romantic and dreamy atmosphere',
            'a confident and empowering mood', 'a nostalgic, retro vibe', 'a summery, carefree feel', 'a sleek and modern atmosphere'
        ],
        'Rhythm/Style': [
            'a simple, repetitive, and danceable beat', 'a classic verse-chorus-bridge song structure',
            'a strong, memorable chorus ("the hook")', 'a pre-chorus that builds tension', 'a steady, predictable rhythm',
            'a syncopated vocal melody over a straight beat', 'a half-time feel in the verses', 'an instrumental break or "drop"',
            'a simple, diatonic chord progression', 'a radio-friendly groove'
        ],
        'Tempo': [
            'a danceable mid-tempo of 100-125 BPM', 'a classic 120 BPM', 'an upbeat, faster tempo around 128 BPM',
            'a slow ballad tempo around 60-75 BPM', 'a driving, energetic tempo', 'a relaxed, swaying tempo',
            'a consistent tempo throughout the song', 'a radio-friendly, toe-tapping tempo', 'a four-on-the-floor pulse', 'a modern, trap-influenced pop tempo'
        ],
        'Key': [
            'a major key (C major, G major)', 'a simple, 4-chord progression (e.g., I-V-vi-IV)',
            'a focus on a strong, singable melody', 'vocal harmonies and layers', 'a memorable melodic hook',
            'predictable and satisfying harmonic resolution', 'a diatonic, "in-key" feel', 'a simple and repetitive harmonic structure',
            'a key that suits a high vocal range', 'a bright, major-scale sound'
        ],
        'Production/Features': [
            'a polished, crisp, and modern production', 'heavily compressed for maximum loudness',
            'autotuned and perfectly tuned vocals', 'a wide stereo field with lots of ear candy', 'a clean, uncluttered mix',
            'use of side-chain compression (pumping effect)', 'a bass-heavy and punchy low end', 'layered synthesizers and samples',
            'a "larger than life" sound', 'a focus on perfection and clarity'
        ],
        'Negative Prompts': [
            'NO heavy guitar distortion', 'NOT overly complex or experimental', 'NO long, improvised instrumental solos',
            'NO raw, lo-fi production', 'NO complex time signatures', 'NO guttural or screaming vocals',
            'NOT acoustic and stripped-down', 'NO dissonant or atonal harmony', 'NOT a live band feel', 'NO ambiguous song structure'
        ]
    },
    # ==================== Reggae ====================
    'reggae': {
        'Instruments': [
            'an off-beat guitar "skank" (on beats 2 and 4)', 'a deep, heavy, and melodic bassline',
            'a "one-drop" drum pattern (kick and snare on beat 3)', 'a "steppers" drum pattern (kick on every beat)',
            'a Hammond organ "bubble" pattern', 'a piano playing off-beat chords', 'a brass section (trumpet, trombone) playing melodies',
            'Latin percussion like bongos and timbales', 'a soulful lead vocal', 'call-and-response backing vocals', 'a clavinet playing skank patterns'
        ],
        'Mood/Atmosphere': [
            'a relaxed, sunny, and positive vibe', 'a chill and meditative feel', 'a conscious, political, or spiritual message',
            'a groovy, danceable feel (for dancehall)', 'a hypnotic and dubby atmosphere', 'a sense of community and unity',
            'a laid-back, "irie" feeling', 'a rootsy, earthy feel', 'a romantic "lovers rock" mood', 'a protest or revolutionary mood'
        ],
        'Rhythm/Style': [
            'a heavy emphasis on beat 3 of the bar (the "one drop")', 'the guitar and piano skank on the off-beats',
            'a deep, grooving bassline as the rhythmic and melodic anchor', 'a syncopated rhythm section',
            'a sparse, spacious rhythmic feel', 'a "riddim" (reusable instrumental track)', 'a rockers or steppers beat',
            'a hypnotic, repetitive groove', 'a slow, swaying rhythm', 'a more upbeat dancehall rhythm'
        ],
        'Tempo': [
            'a relaxed, slow tempo of 60-80 BPM', 'a very laid-back 70 BPM', 'a moderate, danceable tempo for dancehall (90-100 BPM)',
            'a steady, hypnotic tempo', 'a slow, swaying groove', 'a "one drop" tempo', 'a lazy, unhurried pace',
            'a solid, grounded tempo', 'a chilled-out tempo', 'a skanking tempo'
        ],
        'Key': [
            'a minor key (A minor, G minor)', 'simple chord progressions (often just two chords)',
            'a bassline that acts as the main melody', 'a focus on groove over harmonic complexity',
            'call-and-response vocal melodies', 'a soulful, melodic vocal style', 'simple, diatonic harmony',
            'a modal feel', 'a repetitive harmonic structure', 'a key that feels "heavy" or "deep"'
        ],
        'Production/Features': [
            'a distinct Caribbean production style', 'heavy use of tape echo and spring reverb (dub style)',
            'a bass-heavy mix where the bass is the loudest element', 'a raw, analog sound',
            'the use of sound effects like sirens and samples', 'a spacious mix with a clear separation of instruments',
            'a focus on the "riddim" track', 'a production style pioneered at Studio One or by King Tubby',
            'a warm, saturated sound', 'a live band feel'
        ],
        'Negative Prompts': [
            'NO aggressive metal guitars', 'NOT a fast tempo', 'NO shuffle rhythm', 'NO complex chord progressions',
            'NO orchestral strings', 'NOT a polished pop production', 'NO screaming vocals', 'NO blast beats',
            'NOT a four-on-the-floor beat', 'NO intricate, fast solos'
        ]
    },
    # ==================== Rock ====================
    'rock': {
        'Instruments': [
            'an iconic electric guitar riff using power chords', 'a driving, solid bass guitar playing root notes',
            'a hard-hitting acoustic drum kit (kick, snare, cymbals)', 'a powerful, anthemic lead vocal',
            'a melodic and memorable guitar solo', 'a Hammond organ for a classic rock feel',
            'a simple piano part', 'layered rhythm guitars', 'energetic backing vocals', 'a Fender Stratocaster or Gibson Les Paul tone'
        ],
        'Mood/Atmosphere': [
            'energetic and anthemic', 'rebellious, raw, and defiant', 'a classic, nostalgic rock vibe',
            'a driving, road-trip feel', 'a powerful, stadium-filling sound', 'an introspective and angsty mood (alternative rock)',
            'a fun, party-like atmosphere', 'a serious and epic feel', 'a bluesy, swaggering mood', 'a raw, garage-rock feel'
        ],
        'Rhythm/Style': [
            'a driving eighth-note drum beat', 'a simple, hard-hitting 4/4 rhythm', 'a guitar riff-driven structure',
            'a strong backbeat (emphasis on beats 2 and 4)', 'a classic verse-chorus structure',
            'a blues-based shuffle rhythm', 'a powerful, straight-ahead beat', 'a syncopated rock groove',
            'a dynamic build-up from verse to chorus', 'a tight, locked-in rhythm section'
        ],
        'Tempo': [
            'an energetic mid-to-fast tempo of 120-150 BPM', 'a classic rock tempo of 120 BPM',
            'a fast, driving punk tempo of 180+ BPM', 'a slow, powerful ballad tempo around 70 BPM',
            'a solid, head-nodding groove', 'a driving, relentless tempo', 'a moderate, cruising tempo',
            'a stomping, powerful tempo', 'an upbeat, feel-good tempo', 'a powerful, slow-burning tempo'
        ],
        'Key': [
            'a major key (A major, E major)', 'a minor key (E minor, A minor)', 'based on the blues pentatonic scale',
            'simple, powerful chord progressions', 'a focus on strong, memorable guitar riffs',
            'a catchy, sing-along vocal melody', 'use of power chords (root and fifth)', 'a straightforward, diatonic feel',
            'a blues-based harmony', 'a key that is easy to play on guitar'
        ],
        'Production/Features': [
            'a classic Marshall or Fender amplifier tone', 'the sound of a live band playing together in a room',
            'a big, stadium rock sound with natural reverb', 'a raw, "garage" production with minimal effects',
            'a powerful, centered drum sound', 'a clear and present lead vocal', 'a guitar-centric mix',
            'an analog, tape-recorded sound', 'a punchy, dynamic mix', 'a timeless, classic production'
        ],
        'Negative Prompts': [
            'NO synthesizers or drum machines (in classic rock)', 'NO disco beats', 'NOT overly polished or clean',
            'NO complex jazz harmony', 'NO autotuned vocals', 'NO rapping', 'NO orchestral arrangements',
            'NO delicate, fragile sounds', 'NOT minimalist', 'NO ambient soundscapes'
        ]
    }
}

def create_randomized_prompt(genre_name, db):
    """
    為指定的音樂風格生成一個隨機組合的特色描述。

    Args:
        genre_name (str): 音樂風格的名稱 (e.g., 'rock')。
        db (dict): 包含音樂風格特徵的資料庫。

    Returns:
        str: 一個格式為 "音樂風格: 音樂特色" 的字串，如果風格不存在則返回錯誤訊息。
    """
    genre_name_lower = genre_name.lower()
    
    if genre_name_lower not in db:
        return f"{genre_name}: 風格未在資料庫中找到。"

    # 獲取該風格的所有特徵分類
    genre_data = db[genre_name_lower]
    
    # 從每個分類的選項列表中隨機選擇一項
    chosen_features = [random.choice(options) for options in genre_data.values()]
    
    # 將所有選中的特色組合成一個字串
    feature_text = ", ".join(chosen_features)
    
    return f"{genre_name}: {feature_text}"

def generate_optimized_prompts():
    optimized_prompts = {}
    all_genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    for genre in all_genres:
        # 確保您的 music_genre_database 包含所有這些風格的資料
        if genre not in music_genre_database:
            music_genre_database[genre] = music_genre_database['rock']  # 範例：如果資料不完整，暫用rock代替
        
        prompt = create_randomized_prompt(genre, music_genre_database)
        optimized_prompts[genre] = prompt
    
    return optimized_prompts