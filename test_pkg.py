from chkpkg import Package

if __name__ == "__main__":
    with Package() as pkg:
        pkg.run_python_code(
            'from lighthash import file_to_hash_equidistant, '
            'file_to_hash_fibonacci, HashAlgo')

    print("\nPackage is OK!")
