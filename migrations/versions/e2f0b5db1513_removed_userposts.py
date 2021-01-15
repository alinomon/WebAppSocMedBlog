"""removed userposts

Revision ID: e2f0b5db1513
Revises: 0b3e3bcec0d8
Create Date: 2021-01-13 17:38:57.516211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2f0b5db1513'
down_revision = '0b3e3bcec0d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_posts')
    op.add_column('blog_posts', sa.Column('owner', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_posts', 'owner')
    op.create_table('user_posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('owner', sa.VARCHAR(length=200), nullable=True),
    sa.Column('title', sa.VARCHAR(length=100), nullable=True),
    sa.Column('blogBody', sa.VARCHAR(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###