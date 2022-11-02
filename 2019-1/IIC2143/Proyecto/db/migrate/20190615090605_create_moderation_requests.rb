# frozen_string_literal: true

class CreateModerationRequests < ActiveRecord::Migration[5.1]
  def change
    create_table :moderation_requests do |t|
      t.references :user, foreign_key: true
      t.references :course, foreign_key: true
      t.text :description
      t.string :photo

      t.timestamps
    end
  end
end
