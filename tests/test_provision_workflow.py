"""Tests for the provisioning workflow configuration."""

from pathlib import Path


WORKFLOW_PATH = (
    Path(__file__).parent.parent / ".github" / "workflows" / "provision-new-repo.yml"
)


def test_workflow_uses_current_repository_owner():
    content = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert "owner: ${{ github.repository_owner }}" in content
    assert '--org "${{ github.repository_owner }}"' in content
    assert 'https://github.com/${{ github.repository_owner }}/$INPUT_REPO_NAME' in content


def test_workflow_accepts_both_client_id_and_legacy_app_id_credentials():
    content = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert (
        "client-id: ${{ vars.PROVISIONER_APP_CLIENT_ID || secrets.PROVISIONER_APP_CLIENT_ID || vars.PROVISIONER_APP_ID || secrets.PROVISIONER_APP_ID }}"
        in content
    )
    assert "private-key: ${{ secrets.PROVISIONER_APP_PRIVATE_KEY }}" in content
