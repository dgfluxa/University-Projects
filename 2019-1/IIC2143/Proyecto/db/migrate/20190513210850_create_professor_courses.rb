# frozen_string_literal: true

class CreateProfessorCourses < ActiveRecord::Migration[5.1]
  def change
    create_table :professor_courses do |t|
      t.references :course, foreign_key: true
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end
