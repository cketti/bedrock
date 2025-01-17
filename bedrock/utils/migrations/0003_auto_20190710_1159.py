# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 2.2.3 on 2019-07-10 18:59

from django.db import migrations


def fix_bytes_repr(apps, schema_editor):
    """Values were stored as strings with the "b''" in them. This should fix that."""
    GitRepoState = apps.get_model("utils", "GitRepoState")
    for repo in GitRepoState.objects.all():
        if repo.latest_ref.startswith("b'"):
            # strip the b' off the start and the ' off the end
            repo.latest_ref = repo.latest_ref[2:][:-1]
            repo.save()


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0002_auto_20180522_1249"),
    ]

    operations = [migrations.RunPython(fix_bytes_repr)]
