from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / 'frontend' / 'src' / 'lib'))

def test_material_catalogue_contains_pcb_grades():
    import json
    p=Path(__file__).parents[1]/'frontend'/'src'/'data'/'materialCatalogue.js'
    text=p.read_text(encoding='utf-8')
    for grade in ['PCB-PC-MB','PCB-RAM','PCB-CPU-CER','PCB-LOW-APPL','PCB-SERVER']:
        assert grade in text

def test_repository_has_compliance_notes():
    p=Path(__file__).parents[1]/'docs'/'COMPLIANCE_REGISTER.md'
    assert 'POPIA' in p.read_text(encoding='utf-8')
