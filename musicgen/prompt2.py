# ### Prompt 字典 (固定版)
def generate_optimized_prompts():
    """生成針對你的分類器優化的 prompt"""
    optimized_prompts = {
        'blues': """Traditional 12-bar blues with electric guitar string bending, 
           harmonica wailing, slow shuffle rhythm 65 BPM, minor pentatonic scale,
           NOT reggae off-beat, NOT Caribbean style, Delta blues tradition,
           melancholic and soulful, vintage tube amplifier tone""",
        
        'classical': "Classical string quartet, violin melody with cello bass line, piano accompaniment, baroque counterpoint style, concert hall reverb, elegant and refined, moderate tempo 100 BPM, D major key",
        
        'country': "Country ballad with acoustic guitar fingerpicking, steel guitar slides, fiddle melody, storytelling vocal style, rural and nostalgic atmosphere, 3/4 waltz time, 90 BPM, G major key",
        
        'disco': """Classic 1970s disco with orchestral string sections, brass stabs on beats 2 and 4, 
           four-on-the-floor kick drum, syncopated bass guitar with slap technique, 
           125 BPM dance tempo, NOT hip-hop style, NOT rap music, 
           Saturday Night Fever era production, uplifting and energetic""",
        
        'hiphop': """Modern hip-hop with 808 kick drum, trap-influenced hi-hat rolls, 
            sub-bass frequencies, minimal harmonic content, 85 BPM tempo,
            NOT disco strings, NOT four-on-the-floor pattern,
            urban street atmosphere, quantized rhythm programming""",
        
        'jazz': "Jazz standard with tenor saxophone lead, piano comping, walking upright bass, swing drum pattern, sophisticated chord changes, improvisational feel, 130 BPM, F major",
        
        'metal': "Heavy metal with palm-muted electric guitars, power chord progressions, double bass drum, aggressive and intense, fast tempo 150 BPM, E minor, high-gain distortion",
        
        'pop': "Contemporary pop with synthesizer lead melody, clean electric guitar arpeggios, steady four-four drum beat, bright and commercial production, 110 BPM, C major key",
        
        'reggae': "Classic reggae with off-beat guitar skank, bass emphasis on beats 1 and 3, one-drop drum pattern, relaxed tempo 75 BPM, Caribbean style, A minor key",
        
        'rock': "Classic rock with electric guitar power chords, driving eighth-note drum beat, bass guitar root notes, energetic and anthemic, 135 BPM, A major, Marshall amp tone"
    }
    
    return optimized_prompts