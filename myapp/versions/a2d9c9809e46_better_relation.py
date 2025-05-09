"""better relation

Revision ID: a2d9c9809e46
Revises: 202ef9419527
Create Date: 2025-04-20 13:15:46.264802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2d9c9809e46'
down_revision: Union[str, None] = '202ef9419527'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'document', ['doc_id'])
    op.drop_constraint('document_doc_type_id_fkey', 'document', type_='foreignkey')
    op.create_foreign_key(None, 'document', 'doc_type', ['doc_type_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'document', type_='foreignkey')
    op.create_foreign_key('document_doc_type_id_fkey', 'document', 'doc_type', ['doc_type_id'], ['id'])
    op.drop_constraint(None, 'document', type_='unique')
    # ### end Alembic commands ###
