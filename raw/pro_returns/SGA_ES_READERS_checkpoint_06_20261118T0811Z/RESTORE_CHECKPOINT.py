#!/usr/bin/env python3
"""Restore every file from this complete checkpoint and verify its original hash."""
import csv,hashlib,pathlib,shutil,tarfile
root=pathlib.Path(__file__).resolve().parent
def local(name):
 p=pathlib.PurePosixPath(name)
 if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe checkpoint path')
 return root.joinpath(*p.parts)
def put(name,data):
 p=local(name)
 if p.exists():
  if p.read_bytes()!=data:raise ValueError('Refusing to replace a changed file: '+name)
 else:
  p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
with tarfile.open(root/'CHECKPOINT_CONTENTS.tar.xz','r:xz') as t:
 for m in t:
  if not m.isfile():raise ValueError('Unexpected archive member')
  put(m.name,t.extractfile(m).read())
with (root/'CHECKPOINT_DUPLICATES.tsv').open(encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f,delimiter='\t'):
  data=local(r['canonical_path']).read_bytes()
  if hashlib.sha256(data).hexdigest()!=r['sha256']:raise ValueError('Damaged canonical file')
  put(r['path'],data)
count=0
with (root/'CHECKPOINT_MANIFEST.tsv').open(encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f,delimiter='\t'):
  data=local(r['path']).read_bytes()
  if len(data)!=int(r['bytes']) or hashlib.sha256(data).hexdigest()!=r['sha256']:raise ValueError('Verification failed: '+r['path'])
  count+=1
print('Restored and verified every original snapshot file:',count)
