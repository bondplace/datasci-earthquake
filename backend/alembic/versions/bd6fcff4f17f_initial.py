"""Initial

Revision ID: bd6fcff4f17f
Revises: 
Create Date: 2024-12-30 23:02:59.823658

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision: str = "bd6fcff4f17f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_geospatial_table(
        "addresses",
        sa.Column("eas_fullid", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("unit_number", sa.String(), nullable=True),
        sa.Column("address_number", sa.Integer(), nullable=False),
        sa.Column("street_name", sa.String(), nullable=False),
        sa.Column("street_type", sa.String(), nullable=True),
        sa.Column("parcel_number", sa.String(), nullable=True),
        sa.Column("block", sa.String(), nullable=True),
        sa.Column("lot", sa.String(), nullable=True),
        sa.Column("cnn", sa.Integer(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("zip_code", sa.Integer(), nullable=False),
        sa.Column(
            "point",
            Geometry(
                geometry_type="POINT",
                srid=4326,
                spatial_index=False,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                nullable=False,
            ),
            nullable=False,
        ),
        sa.Column("supdist", sa.String(length=255), nullable=True),
        sa.Column("supervisor", sa.Integer(), nullable=True),
        sa.Column("supname", sa.String(length=255), nullable=True),
        sa.Column("nhood", sa.String(length=255), nullable=False),
        sa.Column("sfdata_as_of", sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            "created_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("eas_fullid"),
    )
    op.create_geospatial_index(
        "idx_addresses_point",
        "addresses",
        ["point"],
        unique=False,
        postgresql_using="gist",
        postgresql_ops={},
    )
    op.create_geospatial_table(
        "landslide_zones",
        sa.Column("identifier", sa.Integer(), nullable=False),
        sa.Column(
            "geometry",
            Geometry(
                geometry_type="MULTIPOLYGON",
                srid=4326,
                spatial_index=False,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                nullable=False,
            ),
            nullable=False,
        ),
        sa.Column("gridcode", sa.Integer(), nullable=False),
        sa.Column("sum_shape", sa.Float(), nullable=False),
        sa.Column("shape_length", sa.Float(), nullable=False),
        sa.Column("shape_length_1", sa.Float(), nullable=False),
        sa.Column("shape_area", sa.Float(), nullable=False),
        sa.Column(
            "update_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("identifier"),
    )
    op.create_geospatial_index(
        "idx_landslide_zones_geometry",
        "landslide_zones",
        ["geometry"],
        unique=False,
        postgresql_using="gist",
        postgresql_ops={},
    )
    op.create_geospatial_table(
        "liquefaction_zones",
        sa.Column("identifier", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "geometry",
            Geometry(
                geometry_type="MULTIPOLYGON",
                srid=4326,
                spatial_index=False,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                nullable=False,
            ),
            nullable=False,
        ),
        sa.Column("liq", sa.String(), nullable=False),
        sa.Column("shape_length", sa.Float(), nullable=False),
        sa.Column("shape_area", sa.Float(), nullable=False),
        sa.Column(
            "update_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("identifier"),
    )
    op.create_geospatial_index(
        "idx_liquefaction_zones_geometry",
        "liquefaction_zones",
        ["geometry"],
        unique=False,
        postgresql_using="gist",
        postgresql_ops={},
    )
    op.create_geospatial_table(
        "seismic_hazard_zones",
        sa.Column("identifier", sa.Integer(), nullable=False),
        sa.Column(
            "geometry",
            Geometry(
                geometry_type="MULTIPOLYGON",
                srid=4326,
                spatial_index=False,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                nullable=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "update_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("identifier"),
    )
    op.create_geospatial_index(
        "idx_seismic_hazard_zones_geometry",
        "seismic_hazard_zones",
        ["geometry"],
        unique=False,
        postgresql_using="gist",
        postgresql_ops={},
    )
    op.create_geospatial_table(
        "soft_story_properties",
        sa.Column("identifier", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("block", sa.String(length=255), nullable=True),
        sa.Column("lot", sa.String(length=255), nullable=True),
        sa.Column("parcel_number", sa.String(length=255), nullable=True),
        sa.Column("property_address", sa.String(length=255), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("tier", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.Column("bos_district", sa.Integer(), nullable=True),
        sa.Column(
            "point",
            Geometry(
                geometry_type="POINT",
                srid=4326,
                spatial_index=False,
                from_text="ST_GeomFromEWKT",
                name="geometry",
            ),
            nullable=True,
        ),
        sa.Column("sfdata_as_of", sa.DateTime(timezone=True), nullable=True),
        sa.Column("sfdata_loaded_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "update_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("identifier"),
    )
    op.create_geospatial_index(
        "idx_soft_story_properties_point",
        "soft_story_properties",
        ["point"],
        unique=False,
        postgresql_using="gist",
        postgresql_ops={},
    )
    op.create_geospatial_table(
        "tsunami_zones",
        sa.Column("identifier", sa.Integer(), nullable=False),
        sa.Column("evacuate", sa.String(length=255), nullable=False),
        sa.Column("county", sa.String(length=255), nullable=False),
        sa.Column("global_id", sa.String(length=255), nullable=False),
        sa.Column("shape_length", sa.Float(), nullable=True),
        sa.Column("shape_area", sa.Float(), nullable=True),
        sa.Column(
            "geometry",
            Geometry(
                geometry_type="MULTIPOLYGON",
                srid=4326,
                spatial_index=False,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                nullable=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "update_timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("identifier"),
    )
    op.create_geospatial_index(
        "idx_tsunami_zones_geometry",
        "tsunami_zones",
        ["geometry"],
        unique=False,
        postgresql_using="gist",
        postgresql_ops={},
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_geospatial_index(
        "idx_tsunami_zones_geometry",
        table_name="tsunami_zones",
        postgresql_using="gist",
        column_name="geometry",
    )
    op.drop_geospatial_table("tsunami_zones")
    op.drop_geospatial_index(
        "idx_soft_story_properties_point",
        table_name="soft_story_properties",
        postgresql_using="gist",
        column_name="point",
    )
    op.drop_geospatial_table("soft_story_properties")
    op.drop_geospatial_index(
        "idx_seismic_hazard_zones_geometry",
        table_name="seismic_hazard_zones",
        postgresql_using="gist",
        column_name="geometry",
    )
    op.drop_geospatial_table("seismic_hazard_zones")
    op.drop_geospatial_index(
        "idx_liquefaction_zones_geometry",
        table_name="liquefaction_zones",
        postgresql_using="gist",
        column_name="geometry",
    )
    op.drop_geospatial_table("liquefaction_zones")
    op.drop_geospatial_index(
        "idx_landslide_zones_geometry",
        table_name="landslide_zones",
        postgresql_using="gist",
        column_name="geometry",
    )
    op.drop_geospatial_table("landslide_zones")
    op.drop_geospatial_index(
        "idx_addresses_point",
        table_name="addresses",
        postgresql_using="gist",
        column_name="point",
    )
    op.drop_geospatial_table("addresses")
    # ### end Alembic commands ###
