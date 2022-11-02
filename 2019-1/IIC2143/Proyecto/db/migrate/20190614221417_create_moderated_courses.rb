# frozen_string_literal: true

class CreateModeratedCourses < ActiveRecord::Migration[5.1]
  def change
    create_table :moderated_courses do |t|
      t.references :user, foreign_key: true
      t.references :course, foreign_key: true

      t.timestamps
    end
  end
end
