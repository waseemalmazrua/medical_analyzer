"""add profile creation trigger

Revision ID: PUT_YOUR_NEW_REVISION_HERE
Revises: 6715e51adc8f
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "6715e51adc8f"
down_revision: Union[str, Sequence[str], None] = "6715e51adc8f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the function and trigger for new user profiles."""

    op.execute(
        """
        CREATE OR REPLACE FUNCTION public.handle_new_user()
        RETURNS TRIGGER
        LANGUAGE plpgsql
        SECURITY DEFINER
        SET search_path = ''
        AS $$
        BEGIN
            INSERT INTO public.profiles (
                id,
                full_name,
                created_at
            )
            VALUES (
                NEW.id,
                NEW.raw_user_meta_data ->> 'full_name',
                NOW()
            );

            RETURN NEW;
        END;
        $$;
        """
    )

    op.execute(
        """
        CREATE TRIGGER on_auth_user_created
        AFTER INSERT ON auth.users
        FOR EACH ROW
        EXECUTE FUNCTION public.handle_new_user();
        """
    )


def downgrade() -> None:
    """Remove the profile trigger and function."""

    op.execute(
        """
        DROP TRIGGER IF EXISTS on_auth_user_created
        ON auth.users;
        """
    )

    op.execute(
        """
        DROP FUNCTION IF EXISTS public.handle_new_user();
        """
    )